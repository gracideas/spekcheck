import configparser
import musicbrainzngs

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
version = config['musicbrainz']['version'] 
email = config['musicbrainz']['email']

# Connect this to web form
id_input = "ef49c461-0948-4c57-9baa-8fbb15f0e05b"


# Identify app to MusicBrainz
musicbrainzngs.set_useragent('SpekCheck', version, contact=email)
musicbrainzngs.set_rate_limit(limit_or_interval=1.0, new_requests=1)

try:
    result = musicbrainzngs.get_release_by_id(id_input, includes=["artists", "discids","labels"])
except WebServiceError as exc:
    print("Something went wrong with the request: %s" % exc)
else:
    # Fetches fields from 'result' dictionary
    release = result["release"]
    title = release["title"]
    artist_credit = release["artist-credit"][0]["artist"]["name"]
    physical_format = release["medium-list"][0]["format"]
    catalog_number = release["label-info-list"][0]["catalog-number"]

    # Return values to DB
    print('title: ' + title)
    print('artist: ' + artist_credit)
    print('physical format: '+ physical_format)
    print ('catalog number: ' + catalog_number)







