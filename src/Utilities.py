import sys

sys.path.append('/usr/lib/wasp/')
from Colors import Colors


class Utilities:
    @staticmethod
    def is_hex_color(string):
        """
        Checks to see if string is a hex color
        :param string: user input, checking for validity
        :return: True if string is 3 or 6 characters, or false otherwise
        """
        try:
            int(string, 16)
        except ValueError:
            return False
        return len(string) == 3 or len(string) == 6

    @staticmethod
    def is_valid_lang_code(string):
        """Validates user-inputted lang code"""
        valid_langs = ["ab", "aa", "af", "ak", "sq", "am", "ar", "an", "hy", "as", "av", "ae", "ay", "az", "bm", "ba",
                       "eu", "be", "bn", "bh", "bi", "bs", "br", "bg", "my", "ca", "ch", "ce", "ny", "zh", "zh-Hans",
                       "zh-Hant", "cv", "kw", "co", "cr", "hr", "cs", "da", "dv", "nl", "dz", "en", "eo", "et", "ee",
                       "fo", "fj", "fi", "fr", "ff", "gl", "gd", "gv", "ka", "de", "el", "kl", "gn", "gu", "ht", "ha",
                       "he", "hz", "hi", "ho", "hu", "is", "io", "ig", "id", "in", "ia", "ie", "iu", "ik", "ga", "it",
                       "ja", "jv", "kl", "kn", "kr", "ks", "kk", "km", "ki", "rw", "rn", "ky", "kv", "kg", "ko", "ku",
                       "kj", "lo", "la", "lv", "li", "ln", "lt", "lu", "lg", "lb", "gv", "mk", "mg", "ms", "ml", "mt",
                       "mi", "mr", "mh", "mo", "mn", "na", "nv", "ng", "nd", "ne", "no", "nb", "nn", "ii", "oc", "oj",
                       "cu", "or", "om", "os", "pi", "ps", "fa", "pl", "pt", "pa", "qu", "rm", "ro", "ru", "se", "sm",
                       "sg", "sa", "sr", "sh", "st", "tn", "sn", "ii", "sd", "si", "ss", "sk", "sl", "so", "nr", "es",
                       "su", "sw", "ss", "sv", "tl", "ty", "tg", "ta", "tt", "te", "th", "bo", "ti", "to", "ts", "tr",
                       "tk", "tw", "ug", "uk", "ur", "uz", "ve", "vi", "vo", "wa", "cy", "wo", "fy", "xh", "yi", "ji",
                       "yo", "za", "zu", "ar-ae", "ar-bh", "ar-dz", "ar-eg", "ar-iq", "ar-jo", "ar-kw", "ar-lb",
                       "ar-ly", "ar-ma", "ar-om", "ar-qa", "ar-sa", "ar-sy", "ar-tn", "ar-ye", "de-at", "de-ch",
                       "de-li", "de-lu", "en-au", "en-bz", "en-ca", "en-gb", "en-ie", "en-jm", "en-nz", "en-tt",
                       "en-us", "en-za", "es-ar", "es-bo", "es-cl", "es-co", "es-cr", "es-do", "es-ec", "es-gt",
                       "es-hn", "es-mx", "es-ni", "es-pa", "es-pe", "es-pr", "es-py", "es-sv", "es-uy", "es-ve",
                       "fr-be", "fr-ca", "fr-ch", "fr-lu", "it-ch", "nl-be", "pt-br", "ro-md", "ru-md", "sb", "sv-fi",
                       "zh-cn", "zh-hk", "zh-sg", "zh-tw"]
        if string in valid_langs:
            return True
        else:
            return False

    @staticmethod
    def on(options, args):
        """ Inject colorized indicators ('M' and/or 'P') into input prompts, depending on whether user is creating package and/or manifest. """
        return_options = "["
        for i, s in enumerate(options):
            if s == "M" and args.manifest:
                return_options += Colors.OKGREEN + "M" + Colors.ENDC
            elif s == "P" and args.package:
                return_options += Colors.OKGREEN + "P" + Colors.ENDC
            else:
                return_options += s

            if i < len(options) - 1:
                return_options += " "
        return return_options + "]"
