from nodestream_plugin_dotenv.plugin import DotEnvProjectPlugin


def test_plugin_activate_no_env_set(mocker):
    loader = mocker.patch("nodestream_plugin_dotenv.plugin.load_dotenv")
    subject = DotEnvProjectPlugin()
    subject.before_project_load(None)
    loader.assert_called_once_with(".env")


def test_plugin_activate_env_set(mocker):
    mocker.patch.dict("os.environ", {"NODESTREAM_DOTENV_PATH": ".env.test"})
    loader = mocker.patch("nodestream_plugin_dotenv.plugin.load_dotenv")
    subject = DotEnvProjectPlugin()
    subject.before_project_load(None)
    loader.assert_called_once_with(".env.test")
