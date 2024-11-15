from core.cli.cli_controller import CliController
from core.providers.service_provider import ServiceProvider
from core.plugins.plugin_handler import initialize as initialize_plugins

if __name__ == "__main__":
    plugins = initialize_plugins([
        'plugins', 
        'plugins/techka-secret'
    ])({
        "service_provider": ServiceProvider()
    })
        
    cli_handler = CliController(plugins)

    cli_handler.execute()
