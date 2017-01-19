# The requests module is used to visit web pages from Python
import requests
import yagmail


def send_email(recipient, subject, body):

    # Intialize yagmail
    # still confused about the username/password piece here - is what's in the () username/password? or is it stored in a .yagmail file somewhere else?
    yag = yagmail.SMTP('wcc.python', 'montypython932');

    # Send the email
    yag.send(recipient, subject, body)


def load_site(url):

    # Send a request to the given URL; store the results in a variable called `response`
    response = requests.get(url)

    # A response will contain multiple parts such as a header, an encoding type,
    # and the actual body of the response, referred to as `content`
    # This is what we want, so we extract it from the response.
    web_page_content = response.content

    # Return the content, transformed to all lowercase characters using the .lower() method
    # This will allow our searches of this content to be case insensitive
    return web_page_content.lower()

# Test
#print load_site('https://www.travelzoo.com/top20')

def search_for_vacations(destination, url):

    # Convert destination to lowercase so search is case insensitive
    destination = destination.lower()

    content = load_site(url)

    print('Searching for: ' + destination + '\nChecking site: ' + url)

    if destination in content:
        print('-> FOUND! ')

        # Send email
        recipient = 'nancy.eckenthal@gmail.com'  # Update with your email address
        subject = 'Vacation deal found for ' + destination + '!'
        body = 'Quick! Check out ' + url + ' -- they just posted a deal for a trip to ' + destination + '.'
        send_email(recipient, subject, body)

    else:
        print('-> Not found ')

search_for_vacations('Versailles', 'https://www.travelzoo.com/top20')
#search_for_vacations('France', 'https://www.kayak.com/flights')