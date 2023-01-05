from .accessor import Accessor
from .default_config import ttally_config_path

accessor = Accessor(
    name="ttally",
    module_name="ttally.config",
    config_file=ttally_config_path,
    extension=None,
)


def main() -> None:
    accessor.cli_wrap(prog_name="ttally")


if __name__ == "__main__":
    main()
