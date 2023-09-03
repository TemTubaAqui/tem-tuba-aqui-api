from typing import Any, Optional
from django.core.management import BaseCommand, call_command

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        call_command("migrate")
        call_command("collectstatic", "--noinput")
        call_command("loaddata", "root")
        call_command("loaddata", "attacks")