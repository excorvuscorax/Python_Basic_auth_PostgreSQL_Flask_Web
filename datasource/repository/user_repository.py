from datasource.database import db
from datasource.mapper.user_mapper import UserMapper
from datasource.model.user import User as DatasourceUser

from domain.model.user import User as DomainUser


class UserRepository:

    def __init__(
        self,
        mapper: UserMapper,
    ):
        self._mapper = mapper

    def save(
        self,
        domain_user: DomainUser,
    ) -> None:

        datasource_user = self._mapper.to_datasource(domain_user)

        db.session.add(datasource_user)
        db.session.commit()

    def find_by_login(
        self,
        login: str,
    ) -> DomainUser | None:

        datasource_user = DatasourceUser.query.filter_by(login=login).first()

        if datasource_user is None:
            return None

        return self._mapper.to_domain(datasource_user)

    def find_by_id(
        self,
        user_id: str,
    ) -> DomainUser | None:

        datasource_user = DatasourceUser.query.get(user_id)

        if datasource_user is None:
            return None

        return self._mapper.to_domain(datasource_user)

    def get(
        self,
        user_id: str,
    ) -> DomainUser | None:

        datasource_user = DatasourceUser.query.get(user_id)

        if datasource_user is None:
            return None

        return self._mapper.to_domain(datasource_user)
