from unittest.mock import Mock

import pytest
from grpc import StatusCode

from service.observer_service import ObserverService


class TestObserver:
    @pytest.mark.asyncio
    @pytest.mark.slow
    async def test_create_read_event(self, temp_db):
        request_mock = Mock()
        request_mock.day = 1
        request_mock.name = 'testname'
        request_mock.type = 'testtype'
        request_mock.age_restrictions = 18

        context_mock = Mock()
        context_mock.set_code = Mock()
        context_mock.set_details = Mock()

        service_response = await ObserverService().CreateEvent(
            request=request_mock, context=context_mock
        )
        assert service_response.event.id == 1
        assert service_response.event.name == 'testname'
        context_mock.set_code.assert_not_called()
        context_mock.set_details.assert_not_called()

        request_mock.day = 8

        await ObserverService().CreateEvent(
            request=request_mock, context=context_mock
        )
        context_mock.set_code.assert_called_with(StatusCode.INVALID_ARGUMENT)
        context_mock.set_details.assert_called_with("0 <= day <= 7")

        request_mock.id = 1
        events_list = await ObserverService().ListEvent(
            request=request_mock, context=context_mock
        )
        assert len(events_list.events) == 1
        assert events_list.events[0].id == 1
        assert events_list.events[0].day == 1

        event = await ObserverService().ReadEventById(
            request=request_mock, context=context_mock
        )
        assert event.event.name == 'testname'

        request_mock.name = 'newname'
        event = await ObserverService().UpdateEventById(
            request=request_mock, context=context_mock
        )
        assert event.event.name == 'newname'

        await ObserverService().DeleteEventById(
            request=request_mock, context=context_mock
        )

        events = await ObserverService().ListEvent(
            request=request_mock, context=context_mock
        )
        assert len(events.events) == 0
