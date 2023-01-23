from datetime import date
from src import app, db

from src.database.models import Film, Actor


def drop_films():
    db.session.query(Film).delete()
    db.session.commit()


def drop_actors():
    db.session.query(Actor).delete()
    db.session.commit()


def populate_films():
    the_bourne_identity = Film(
        title='The Bourne Identity',
        release_date=date(2002, 11, 2),
        description='some description',
        distributed_by='Universal Pictures',
        length=113,
        rating=7.8
    )
    the_bourne_supremacy = Film(
        title='The Bourne Supremacy',
        release_date=date(2004, 10, 2),
        description='some description',
        distributed_by='Universal Pictures',
        length=108,
        rating=7.7
    )
    the_bourne_ultimatum = Film(
        title='The Bourne Ultimatum',
        release_date=date(2004, 10, 2),
        description='some description',
        distributed_by='Universal Pictures',
        length=115,
        rating=7.7
    )
    jason_bourne = Film(
        title='Jason Bourne',
        release_date=date(2016, 7, 2),
        description='some description',
        distributed_by='Universal Pictures',
        length=123,
        rating=6.2
    )

    matt_damon = Actor(
        name='Matt Daemon',
        birthday=date(1982, 7, 12),
        is_active=True
    )
    franka_potente = Actor(
        name='Franka Potente',
        birthday=date(1983, 3, 11),
        is_active=True
    )
    julia_stiles = Actor(
        name='Julia Stiles',
        birthday=date(1983, 2, 12),
        is_active=True
    )
    alicia_vikander = Actor(
        name='Alicia Vikander',
        birthday=date(1981, 2, 2),
        is_active=True
    )

    the_bourne_identity.actors = [matt_damon, julia_stiles, franka_potente]
    the_bourne_supremacy.actors = [matt_damon, julia_stiles, franka_potente]
    the_bourne_ultimatum.actors = [matt_damon, julia_stiles]
    jason_bourne.actors = [matt_damon, alicia_vikander]

    db.session.add_all([the_bourne_identity, the_bourne_supremacy, the_bourne_ultimatum, jason_bourne])

    db.session.add_all([matt_damon, franka_potente, julia_stiles, alicia_vikander])
    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    app.app_context().push()
    print(f'Deleting notes in Films ...')
    drop_films()
    print(f'Deleting notes in Actors ...')
    drop_actors()
    print(f'Creating Films...')
    populate_films()
    print(f'Films created')
