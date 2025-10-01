# PRODIGY_SD_03

📇 Contact Manager GUI (Python + Tkinter)
A simple desktop application built with Python and Tkinter to manage your contacts. Easily add, edit, and delete contact entries, which are saved persistently using a JSON file.


🛠 Features
Add new contacts with Name, Phone Number, and Email.

View all saved contacts in a neatly formatted list.

Edit contact details directly from the list.

Delete unwanted contacts with a confirmation prompt.

Persistent storage in a contacts.json file (no database needed).

Simple and intuitive GUI built with Tkinter.

📁 Files
contact_manager_gui.py – Main source code for the GUI and logic.

contacts.json – JSON file automatically created to store your contact data.

🖥 Technologies Used
Python 3.x

Tkinter (for GUI)

JSON (for data storage)


{
"event": "Configuration file loaded: /home/adminuser/venv/lib/python3.11/site-packages/readmeai/config/settings/ignore_list.toml",
"level": "info",
"logger": "readmeai.config.settings",
"timestamp": "2025-10-01T09:14:41.742450Z",
"filename": "settings.py",
"func_name": "_load_settings",
"lineno": 276
}
{
"event": "Configuration file loaded: /home/adminuser/venv/lib/python3.11/site-packages/readmeai/config/settings/languages.toml",
"level": "info",
"logger": "readmeai.config.settings",
"timestamp": "2025-10-01T09:14:41.743191Z",
"filename": "settings.py",
"func_name": "_load_settings",
"lineno": 276
}
{
"event": "Configuration file loaded: /home/adminuser/venv/lib/python3.11/site-packages/readmeai/config/settings/parsers.toml",
"level": "info",
"logger": "readmeai.config.settings",
"timestamp": "2025-10-01T09:14:41.743915Z",
"filename": "settings.py",
"func_name": "_load_settings",
"lineno": 276
}
{
"event": "Configuration file loaded: /home/adminuser/venv/lib/python3.11/site-packages/readmeai/config/settings/prompts.toml",
"level": "info",
"logger": "readmeai.config.settings",
"timestamp": "2025-10-01T09:14:41.744744Z",
"filename": "settings.py",
"func_name": "_load_settings",
"lineno": 276
}
{
"event": "Configuration file loaded: /home/adminuser/venv/lib/python3.11/site-packages/readmeai/config/settings/tool_config.toml",
"level": "info",
"logger": "readmeai.config.settings",
"timestamp": "2025-10-01T09:14:41.749568Z",
"filename": "settings.py",
"func_name": "_load_settings",
"lineno": 276
}
{
"event": "Configuration file loaded: /home/adminuser/venv/lib/python3.11/site-packages/readmeai/config/settings/tooling.toml",
"level": "info",
"logger": "readmeai.config.settings",
"timestamp": "2025-10-01T09:14:41.750990Z",
"filename": "settings.py",
"func_name": "_load_settings",
"lineno": 276
}
{
"event": "Pydantic settings: dict_keys(['config', 'ignore_list', 'languages', 'parsers', 'prompts', 'tool_config', 'tooling'])",
"level": "info",
"logger": "readmeai.cli.main",
"timestamp": "2025-10-01T09:14:41.752508Z",
"filename": "main.py",
"func_name": "main",
"lineno": 86
}
{
"event": "Repository settings: repository='https://github.com/rudrasave/PRODIGY_SD_03' full_name='rudrasave/PRODIGY_SD_03' host_domain='github.com' host='github' name='PRODIGY_SD_03'",
"level": "info",
"logger": "readmeai.cli.main",
"timestamp": "2025-10-01T09:14:41.752657Z",
"filename": "main.py",
"func_name": "main",
"lineno": 87
}
{
"event": "LLM API settings: api='OPENAI' base_url='https://api.openai.com/v1/chat/completions' context_window=3900 encoder='cl100k_base' host_name=Url('https://api.openai.com/') localhost=Url('http://localhost:11434/') model='gpt-3.5-turbo' path='v1/chat/completions' temperature=0.1 tokens=699 top_p=0.9",
"level": "info",
"logger": "readmeai.cli.main",
"timestamp": "2025-10-01T09:14:41.752885Z",
"filename": "main.py",
"func_name": "main",
"lineno": 88
}
{
"event": "Total files analyzed: 1",
"level": "info",
"logger": "readmeai.__main__",
"timestamp": "2025-10-01T09:14:42.264172Z",
"filename": "__main__.py",
"func_name": "log_repository_context",
"lineno": 102
}
{
"event": "Metadata extracted: {'cicd': {}, 'containers': {}, 'documentation': {}, 'package_managers': {}}",
"level": "info",
"logger": "readmeai.__main__",
"timestamp": "2025-10-01T09:14:42.264311Z",
"filename": "__main__.py",
"func_name": "log_repository_context",
"lineno": 103
}
{
"event": "Dependencies: ['python']",
"level": "info",
"logger": "readmeai.__main__",
"timestamp": "2025-10-01T09:14:42.264418Z",
"filename": "__main__.py",
"func_name": "log_repository_context",
"lineno": 104
}
{
"event": "Languages: {'py': 1}",
"level": "info",
"logger": "readmeai.__main__",
"timestamp": "2025-10-01T09:14:42.264527Z",
"filename": "__main__.py",
"func_name": "log_repository_context",
"lineno": 105
}
Traceback (most recent call last):
File "/home/adminuser/venv/lib/python3.11/site-packages/readmeai/__main__.py", line 32, in error_handler
yield
File "/home/adminuser/venv/lib/python3.11/site-packages/readmeai/__main__.py", line 40, in readme_agent
asyncio.run(readme_generator(config, output_file))
File "/usr/lib/python3.11/asyncio/runners.py", line 190, in run
return runner.run(main)
^^^^^^^^^^^^^^^^
File "/usr/lib/python3.11/asyncio/runners.py", line 118, in run
return self._loop.run_until_complete(task)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/lib/python3.11/asyncio/base_events.py", line 653, in run_until_complete
return future.result()
^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/readmeai/__main__.py", line 55, in readme_generator
async with ModelFactory.get_backend(config, context).use_api() as llm:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/readmeai/models/factory.py", line 41, in get_backend
return llm_service(config, context)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/readmeai/models/openai.py", line 31, in __init__
self._model_settings()
File "/home/adminuser/venv/lib/python3.11/site-packages/readmeai/models/openai.py", line 43, in _model_settings
self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/openai/_client.py", line 105, in __init__
raise OpenAIError(
openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
File "/home/adminuser/venv/bin/readmeai", line 8, in <module>
sys.exit(main())
^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/click/core.py", line 1157, in __call__
return self.main(*args, **kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/click/core.py", line 1078, in main
rv = self.invoke(ctx)
^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/click/core.py", line 1434, in invoke
return ctx.invoke(self.callback, **ctx.params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/click/core.py", line 783, in invoke
return __callback(*args, **kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/readmeai/cli/main.py", line 90, in main
readme_agent(config=config, output_file=output)
File "/home/adminuser/venv/lib/python3.11/site-packages/readmeai/__main__.py", line 39, in readme_agent
with error_handler():
File "/usr/lib/python3.11/contextlib.py", line 155, in __exit__
self.gen.throw(typ, value, traceback)
File "/home/adminuser/venv/lib/python3.11/site-packages/readmeai/__main__.py", line 34, in error_handler
raise ReadmeGeneratorError(e) from e
readmeai.errors.ReadmeGeneratorError: Error generating README: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable

