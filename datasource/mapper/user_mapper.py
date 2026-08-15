from datasource.model.user import User as DatasourceUser

from domain.model.user import User as DomainUser


class UserMapper:

    def to_datasource(
        self,
        domain_user: DomainUser,
    ) -> DatasourceUser:

        return DatasourceUser(
            user_id=domain_user.user_id,
            login=domain_user.login,
            password=domain_user.password,
        )

    def to_domain(
        self,
        datasource_user: DatasourceUser,
    ) -> DomainUser:

        return DomainUser(
            user_id=datasource_user.user_id,
            login=datasource_user.login,
            password=datasource_user.password,
        )
