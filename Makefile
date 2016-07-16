default:
	@echo "make something yourself!"

SETUP_FLAG=.env/setup_done

.PHONY: run update superuser shell test test-coverage

$(SETUP_FLAG): requirements.txt
	mkdir .env || true
	virtualenv --python=python3 --no-site-packages --distribute .env
	bash -c "source .env/bin/activate && pip3 install -r requirements.txt"
	touch $(SETUP_FLAG)

run: $(SETUP_FLAG) # start server
	bash -c "source .env/bin/activate && ./manage.py migrate &&\
		cd issues && django-admin compilemessages"
	bash -c "source .env/bin/activate && ./manage.py runserver"

superuser: $(SETUP_FLAG) # create a superuser in the database
	bash -c "source .env/bin/activate && ./manage.py createsuperuser"

shell: $(SETUP_FLAG) # enter shell (use pip3 etc)
	bash -c "source .env/bin/activate && bash"

update: $(SETUP_FLAG) # when requirements.txt changed
	bash -c "source .env/bin/activate && pip3 install -r requirements.txt"

test: $(SETUP_FLAG) # run test suite
	bash -c "source .env/bin/activate && ./manage.py test -v2"

test-coverage: $(SETUP_FLAG) # run test suite with coverage report
	bash -c "source .env/bin/activate && coverage run --source='issues,family_issue_tracker' ./manage.py test -v2 && coverage html && coverage report --skip-covered --fail-under=90"
