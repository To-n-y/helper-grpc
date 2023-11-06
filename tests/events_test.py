from unittest.mock import Mock

import pytest
from grpc import StatusCode

from service.observer_service import ObserverService


class TestObserver:
    @pytest.mark.asyncio
    async def test_create_event(self, temp_db):
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
