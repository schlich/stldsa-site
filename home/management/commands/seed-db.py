import datetime
import logging
from faker import Faker
import factory
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from wagtail.core.models import Page, Site
from events.models import Event
from home.models import HomePage
from news.models import NewsIndexPage
from committees.models import CommitteesPage
from committees.factories import CommitteeFactory

fake = Faker()

User = get_user_model()

logger = logging.getLogger("setup_page_tree")


committee_list = CommitteeFactory.build_batch(8)


class Command(BaseCommand):
    """
    this command is used to create the initial wagtail cms page tree
    """

    help = "creates initial wagtail cms page tree"
    requires_system_checks = False

    def _setup(self):
        # Create a site with the new LanguageRedirectionPage set as the root

        Page.objects.filter(id=2).delete()
        root = Page.get_first_root_node()
        homepage = HomePage(
            title="St Louis DSA",
            banner_title="We are the St. Louis Democratic Socialists of America!",
            body=f"""
            <h3>Our Mission:</h3><p><b>{fake.sentence(10)}</b></p><h3>We
            Believe:</h3><p><b>{fake.sentence(10)}</b></p>
            """,
            highlighted_campaign=f"{' '.join(fake.words(2)).title()} Campaign",
            highlighted_description=fake.paragraph(5),
        )
        root.add_child(instance=homepage)
        site = Site(
            hostname="localhost",
            root_page=homepage,
            is_default_site=True,
            site_name="stldsa.org",
        )
        site.save()
        future_event = Event(
            title="Event Title",
            description=fake.paragraph(),
            start=fake.future_datetime(tzinfo=datetime.timezone.utc),
        )
        future_event.save()

        newsindexpage = NewsIndexPage(title="News", slug="news", show_in_menus=True)
        homepage.add_child(instance=newsindexpage)
        NewsPage = apps.get_model("news.NewsPage")
        newspage = NewsPage(
            title=fake.sentence(),
            date=datetime.date.today(),
            body=fake.paragraph(30),
            show_in_menus=True,
        )
        newsindexpage.add_child(instance=newspage)
        committees = CommitteesPage(
            title="What We Do", slug="formations", show_in_menus=True
        )
        homepage.add_child(instance=committees)
        committee_list = CommitteeFactory.build_batch(8)
        [committees.add_child(instance=committee) for committee in committee_list]
        committees.save()

    def handle(self, raise_error=False, *args, **options):
        # Root Page and a default homepage are created by wagtail migrations
        # so check for > 2 here
        verbosity = options["verbosity"]
        checks = [Page.objects.all().count() > 2]
        if any(checks):
            # YOU SHOULD NEVER RUN THIS COMMAND WITHOUT PRIOR DB DUMP
            raise RuntimeError("Pages exists. Aborting.")

        self._setup()
        if verbosity > 0:
            msg = "Page Tree successfully created."
            self.stdout.write(msg)
