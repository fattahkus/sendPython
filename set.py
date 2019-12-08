from datetime import datetime


LOG_FILENAME = '/tmp/pymailer.log'
CSV_RETRY_FILENAME = '/tmp/pymailer.csv'
STATS_FILE = '/tmp/pymailer-%s.stat' % str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')

SMTP_HOST = 'localhost'
SMTP_PORT = '25'


FROM_NAME = 'Company Name'
FROM_EMAIL = 'company@example.com'


TEST_RECIPIENTS = [
    {'name': 'Name', 'email': 'someone@example.com'},
]