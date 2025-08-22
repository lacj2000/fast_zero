from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_crate_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            email='luizjuniordeveloper@gmail.com',
            username='lacj2000',
            name='Luiz Junior',
            password='unsecpass',
        )

        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'lacj2000'))

    assert asdict(user) == {
        'id': 1,
        'username': 'lacj2000',
        'email': 'luizjuniordeveloper@gmail.com',
        'name': 'Luiz Junior',
        'password': 'unsecpass',
        'created_at': time,
    }
