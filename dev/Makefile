VIRTUAL_ENV ?=

define ERROR_NOT_VENV

	You are trying to install development dependencies
	for py-haproxy-api packege outside Python Virtual
	Envitonment but this is prohibed by project politics.

	Please install Python Virtual Environment, activate it
	and run installation again!

	Example:
		```shell
			python -m virtualenv ${pwd}/../venv
			. ${pwd}/../venv/bin/activate
		```

endef

ifeq ($(strip $(VIRTUAL_ENV)),)
$(error $(ERROR_NOT_VENV) )
else
$(info *** USING PYTHON VIRTUALENV FROM: $(VIRTUAL_ENV) ***)
endif

install:
	@pip install -r requirements.txt
	@pre-commit install
	@pre-commit install-hooks
