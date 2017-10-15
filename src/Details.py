import json
import os
from urllib.parse import urlparse

import sys

sys.path.append('/usr/lib/wasp/')
from Utilities import Utilities
from Colors import Colors


class Details:
    def __init__(self, details: dict, args):
        self.details = details
        self.args = args

    def generate(self):
        if self.args.manifest:
            manifest = {
                "name": self.details['name'],
                "description": self.details['description'],
                "short_name": self.details['short_name'],
                "theme_color": self.details['theme_color'],
                "background_color": self.details['background_color'],
                "start_url": self.details['start_url'],
                "display": self.details['display'],
                "lang": self.details['lang'],
                "orientation": self.details['orientation'],
                "dir": self.details['dir']
            }

            if self.details['related_applications_check'].lower() == 'y':
                manifest["related_applications"] = self.details['related_applications']
                manifest["prefer_related_applications"] = self.details['prefer_related_applications']

            if self.details['icons_check'].lower() == 'y':
                manifest["icons"] = self.details['icons']

            with open('manifest.json', 'w') as fp:
                json.dump(manifest, fp, sort_keys=True, indent=4, separators=(',', ': '))

        if self.args.package:
            package = {
                "name": self.details['name']
            }

            if 'description' in self.details and len(self.details['description']) > 0:
                package['description'] = self.details['description']

            if 'safe_name' in self.details:
                package['name'] = self.details['safe_name']

            if 'keywords' in self.details:
                package['keywords'] = self.details['keywords']

            if "private" in self.details:
                package['private'] = self.details['private']

            bugs = {}
            if 'issue_tracker_url' in self.details and len(self.details['issue_tracker_url']) > 0:
                bugs['url'] = self.details['issue_tracker_url']

            if 'bug_report_email' in self.details and len(self.details['bug_report_email']) > 0:
                bugs['email'] = self.details['bug_report_email']

            if len(bugs) > 0:
                package['bugs'] = bugs

            with open('package.json', 'w') as fp:
                json.dump(package, fp, sort_keys=True, indent=4, separators=(',', ': '))

    def set(self):
        """ Individual method calls prompting user to input specific fields for manifest and/or package. """
        if self.args.manifest or self.args.package:
            self.name()
            self.description()
        if self.args.package:
            self.keywords()
            self.issue_tracker_url()
            self.bug_report_email()
            self.private()
        if self.args.manifest:
            self.short_name()
            self.app_colors('theme_color')
            self.app_colors('background_color')
            self.display()
            self.lang()
            self.dir()
            self.start_url()
            self.orientation()
            self.RelatedApplication(self.details, self.args)
            self.Icon(self.details, self.args)

        return self

    def short_name(self):
        """ Prompt user for short, human-readable name. """
        self.details['short_name'] = input(
            "Short Name " + str(Utilities.on(["M"], self.args)) + " (" + Colors.OKBLUE + self.details['name'][
                                                                                         0:12] + Colors.ENDC + "): ")
        # default to project name
        if self.details['short_name'] == '':
            self.details['short_name'] = self.details['name'][0:12]

    def keywords(self):
        keywords = input("Keywords " + str(Utilities.on(["P"], self.args)) + ":")
        if keywords != '':
            self.details['keywords'] = keywords.split(sep=' ')

    def private(self):
        """ Prompt user for making repository private, public by default"""
        private = input("Do you want to make this repository private? " + str(
                    Utilities.on(["P"], self.args)) + " (y/" + Colors.OKBLUE + "n" + Colors.ENDC + "): ")
        if private.lower() == 'y':
            self.details['private'] = True

    def app_colors(self, color_type):
        """ Prompt user for theme/background color, ensure valid hex value entered. Default for both is white. """
        if color_type == 'theme_color':
            prompt = "Theme Color "
        elif color_type == 'background_color':
            prompt = "Background Color "
        self.details[color_type] = input(
            prompt + str(Utilities.on(["M"], self.args)) + " (" + Colors.OKBLUE + "#FFF" + Colors.ENDC + "): #")
        if self.details[color_type] == "":
            self.details[color_type] = '#FFF'
        elif not Utilities.is_hex_color(self.details[color_type]):
            print("Please enter a valid hex code")
            self.app_colors(color_type)
        else:
            self.details[color_type] = '#' + self.details[color_type].upper()

    def issue_tracker_url(self):
        """ Prompt user for URL to the issue tracker of the project. """
        self.details['issue_tracker_url'] = input(
            "Issue Tracker URL " + str(
                Utilities.on(["P"], self.args)) + " (" + Colors.OKBLUE + "\"\"" + Colors.ENDC + "): ")
        if self.details['issue_tracker_url'] != "":
            if not bool(urlparse(self.details['issue_tracker_url']).scheme):
                print("Please enter a valid issue tracker url")
                self.issue_tracker_url()

    def bug_report_email(self):
        """ Prompt user for the email address to which the bug reports can be sent. """
        self.details['bug_report_email'] = input(
            "Bug Report Email " + str(
                Utilities.on(["P"], self.args)) + " (" + Colors.OKBLUE + "\"\"" + Colors.ENDC + "): ")
        if self.details['bug_report_email'] != "":
            if '@' not in self.details['bug_report_email']:
                print("Please enter a valid email address")
                self.bug_report_email()

    def start_url(self):
        """ Prompt user for URL that loads when application launched. Default is /. """
        self.details['start_url'] = input(
            "Starting URL " + str(Utilities.on(["M"], self.args)) + " (" + Colors.OKBLUE + "/" + Colors.ENDC + "): ")
        if self.details['start_url'] == '':
            self.details['start_url'] = "/"

    def lang(self):
        """ Prompt user for primary language, ensure valid lang code entered. Default is English. """
        default_lang = "en"
        self.details['lang'] = input(
            "Language " + str(
                Utilities.on(["M"], self.args)) + " (" + Colors.OKBLUE + default_lang + Colors.ENDC + "): ")
        if Utilities.is_valid_lang_code(str(self.details['lang'])):
            self.details['lang'] = self.details['lang']
        elif self.details['lang'] == "":
            self.details['lang'] = default_lang
        else:
            print("Please enter a valid language code")
            self.lang()

    def dir(self):
        """ Prompt user for primary text direction for 'name', 'short_name', and 'description' members. Default is 'auto'. """
        dir_val = input("Text Direction " + str(
            Utilities.on(["M"], self.args)) + " (" + Colors.OKBLUE + "auto" + Colors.ENDC + "): ")
        if dir_val.lower() == "ltr" \
                or dir_val.lower() == "rtl" \
                or dir_val.lower() == "auto":
            self.details['dir'] = dir_val.lower()
        elif dir_val == '':
            self.details['dir'] = "auto"

    def display(self):
        """ Prompt user for display mode. Default is 'minimal-ui'. """
        self.details['display'] = input(
            "Display " + str(
                Utilities.on(["M"], self.args)) + " (" + Colors.OKBLUE + "minimal-ui" + Colors.ENDC + "): ")
        if self.details['display'].lower() == "minimal-ui" \
                or self.details['display'].lower() == "browser" \
                or self.details['display'].lower() == "standalone" \
                or self.details['display'].lower() == "fullscreen":
            self.details['display'] = self.details['display'].lower()
        elif self.details['display'] == '':
            self.details['display'] = "minimal-ui"
        else:
            print("Please enter one of the options from https://developer.mozilla.org/en-US/docs/Web/Manifest#display")
            self.display()

    def orientation(self):
        """ Prompt user for orientation of app's top level browsing contexts. Default is 'any'. """
        self.details['orientation'] = input(
            "Display Orientation " + str(
                Utilities.on(["M"], self.args)) + " (" + Colors.OKBLUE + "any" + Colors.ENDC + "): ")
        if self.details['orientation'].lower() == "any" \
                or self.details['orientation'].lower() == "natural" \
                or self.details['orientation'].lower() == "landscape" \
                or self.details['orientation'].lower() == "landscape-primary" \
                or self.details['orientation'].lower() == "landscape-secondary" \
                or self.details['orientation'].lower() == "portrait" \
                or self.details['orientation'].lower() == "portrait-primary" \
                or self.details['orientation'].lower() == "portrait-secondary":
            self.details['orientation'] = self.details['orientation'].lower()
        elif self.details['orientation'] == '':
            self.details['orientation'] = "any"
        else:
            print(
                "Please enter one of the options from https://developer.mozilla.org/en-US/docs/Web/Manifest#orientation")
            self.orientation()

    class Icon:
        """
        Specifies parameters for (optional) icon image.
        Prompts user to add additional icon object to array after each instantiation.
        """

        def __init__(self, details: dict, args):
            self.details = details
            self.args = args
            self.details['icons_check'] = input("Do you want to include Icons? " + str(
                Utilities.on(["M"], args)) + " (y/" + Colors.OKBLUE + "n" + Colors.ENDC + "): ")
            if self.details['icons_check'].lower() == 'y':
                icons = input("Add an Icon? " + str(
                    Utilities.on(["M"], args)) + " (y/" + Colors.OKBLUE + "n" + Colors.ENDC + "): ")
                self.details['icons'] = []

                if icons.lower() == 'y':
                    self.icon()

        def icon_src(self):
            icons_src = input("Image src " + str(Utilities.on(["M"], self.args)) + ": ")
            if icons_src != "":
                if os.path.isfile(icons_src) or bool(urlparse(icons_src).scheme):
                    return icons_src
                else:
                    print("Please enter a valid path or URL")
                    return self.icon_src()

        def icon(self):
            new_icon = {}

            new_icon['src'] = self.icon_src()

            icons_type = input("Type " + str(Utilities.on(["M"], self.args)) + ": ")
            if icons_type != "":
                new_icon['type'] = icons_type.lower()
                # TODO: Validation

            icons_sizes = input("Sizes " + str(Utilities.on(["M"], self.args)) + ": ")
            if icons_sizes != "":
                new_icon['sizes'] = icons_sizes.lower()
                # TODO: Validation

            self.details['icons'].append(new_icon)
            icons = input(
                "Add another Icon? " + str(
                    Utilities.on(["M"], self.args)) + " (y/" + Colors.OKBLUE + "n" + Colors.ENDC + "): ")

            if icons.lower() == 'y':
                self.icon()

    class RelatedApplication:
        """
        Specifies parameters for optional related application object.
        Prompts user to add additional application object to array after each instantiation.
        """

        def __init__(self, details: dict, args):
            self.details = details
            self.args = args
            self.details['related_applications_check'] = input("Do you want to include related applications? " + str(
                Utilities.on(["M"], self.args)) + " (y/" + Colors.OKBLUE + "n" + Colors.ENDC + "): ")
            if self.details['related_applications_check'].lower() == 'y':
                prefer_related_applications = input("Prefer Related Applications? " + str(
                    Utilities.on(["M"], self.args)) + " (y/" + Colors.OKBLUE + "n" + Colors.ENDC + "): ")

                if prefer_related_applications.lower() == 'y':
                    self.details['prefer_related_applications'] = True
                elif prefer_related_applications.lower() == 'n' or prefer_related_applications.lower() == '':
                    self.details['prefer_related_applications'] = False
                related_applications = input("Add a Related Application? " + str(
                    Utilities.on(["M"], self.args)) + " (y/" + Colors.OKBLUE + "n" + Colors.ENDC + "): ")
                self.details['related_applications'] = []

                if related_applications.lower() == 'y':
                    self.related_application()

        def related_application_url(self):
            related_applications_url = input("URL " + str(Utilities.on(["M"], self.args)) + ": ")
            if related_applications_url != "":
                if bool(urlparse(related_applications_url).scheme):
                    return related_applications_url
                else:
                    print("Please enter a valid URL")
                    return self.related_application_url()

        def related_application(self):
            new_related_application = {}

            related_applications_platform = input("Platform " + str(Utilities.on(["M"], self.args)) + ": ")
            if related_applications_platform != "":
                new_related_application['platform'] = related_applications_platform.lower()
                # TODO: Validation

            new_related_application['url'] = self.related_application_url()

            related_applications_id = input("ID " + str(Utilities.on(["M"], self.args)) + ": ")
            if related_applications_id != "":
                new_related_application['id'] = related_applications_id.lower()
                # TODO: Validation

            self.details['related_applications'].append(new_related_application)
            related_applications = input(
                "Add another Related Application? " + str(
                    Utilities.on(["M"], self.args)) + " (y/" + Colors.OKBLUE + "n" + Colors.ENDC + "): ")

            if related_applications.lower() == 'y':
                self.related_application()

    def name(self):
        """ Prompt user for project name. Defaults to current directory name. """
        directory = os.path.basename(os.getcwd())
        self.details['name'] = input(
            "Project/Software Name " + str(Utilities.on(["M", "P"], self.args)) + " (" + Colors.OKBLUE + directory[
                                                                                                         0:45] + Colors.ENDC + "): ")
        if self.details['name'] == '':
            self.details['name'] = directory[0:45]

        # Check if the name is safe for packages
        if self.args.package:
            self.safe_name()

    def safe_name(self):
        """ Validate project name is safe for packages, asking for alternate input if needed. """
        # TODO: Use regex
        if self.details['name'] != (self.details['name'].lower()).replace(" ", "-"):
            self.details['safe_name'] = input(
                "Package Name " + str(Utilities.on(["P"], self.args)) + " (" + Colors.OKBLUE + (self.details[
                                                                                                    'name'].lower()).replace(
                    " ", "-")[0:214] + Colors.ENDC + "): ")
            if self.details['safe_name'] == '':
                self.details['safe_name'] = (self.details['name'].lower()).replace(" ", "-")[0:214]

            if self.details['safe_name'] != (self.details['safe_name'].lower()).replace(" ", "-"):
                print("Package names cannot have uppercase letters or spaces, please try a new name:")
                self.safe_name()
            if len(self.details['safe_name']) > 214:
                print("Package names must less than or equal to 214 characters, please try a new name:")
                self.safe_name()
            if self.details['safe_name'][:1] == "." or self.details['safe_name'][:1] == "_":
                print("Package names cannot begin with a '.' or '_', please try a new name:")
                self.safe_name()

    def description(self):
        """ Prompt user for app description. """
        self.details['description'] = input("Description " + str(Utilities.on(["M", "P"], self.args)) + ": ")
