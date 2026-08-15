from web.model.sign_up_request import SignUpRequest as WebSignUpRequest
from domain.model.sign_up_request import SignUpRequest as DomainSignUpRequest


class UserMapper:

    def to_domain(
        self,
        request: WebSignUpRequest,
    ) -> DomainSignUpRequest:

        return DomainSignUpRequest(
            login=request.login,
            password=request.password,
        )
