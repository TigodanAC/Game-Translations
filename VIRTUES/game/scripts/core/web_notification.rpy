define fetch_web_notifications_enabled = False

init 1 python:

    web_messages = []

    if fetch_web_notifications_enabled:
        
        from requests import Session
        from requests import get as requests_get
        from requests.adapters import HTTPAdapter
        from requests.packages.urllib3.util.retry import Retry
        from urllib.request import getproxies
        
        notification_urls = ["https://virtues-notifications.vercel.app", "https://virtues-notifications.netlify.app", "https://nomeme.neocities.org"]
        
        
        
        def get_web_response(link):
            try:
                session = Session()
                retry = Retry(connect=3, backoff_factor=0.5)
                adapter = HTTPAdapter(max_retries=retry)
                session.mount('http://', adapter)
                session.mount('https://', adapter)
                response = requests_get(link, proxies=getproxies())
                print(response)
                return response
            except Exception as e:
                print(e, e.message)
        
        def parse_web_response(text):
            messages = []
            success = False
            
            for line in text.split("\n\n"):
                message = None
                valid = True
                
                for part in line.split("|"):
                    
                    if part.startswith('v'):
                        req_version = int(re.search(r'\d+', part).group())
                        print("required_version is %s" % req_version)
                        if part.startswith("v>") and config.version > req_version:
                            pass
                        elif part.startswith("v>=") and config.version >= req_version:
                            pass
                        elif part.startswith("v<") and config.version < req_version:
                            pass
                        elif part.startswith("v<=") and config.version <= req_version:
                            pass
                        elif part.startswith("v=") and config.version == req_version:
                            pass
                        else:
                            print("game version does not meet %s." % part)
                            valid = False
                        
                        print("game version meets %s." % part)
                    
                    elif part.startswith("#"):
                        message = part[1:]
                        print("message: %s" % message)
                        success = True
                    
                    else:
                        print("unparsable part: %s" % message)
                
                if valid and message:
                    messages.append(message)
            
            return (success, messages)
        
        def fetch_web_notifications():
            try:
                print("attempting to get notifications...")
                
                for url in notification_urls:
                    print("url: %s" % url)    
                    response = get_web_response(url)
                    
                    if response and response.status_code == 200 and response.text:
                        print("responese fetched.")
                        attempt = parse_web_response(response.text)
                        success = attempt[0]
                        messages = attempt[1]
                        if success:
                            store.web_messages = messages
                            print('parse succeeded.\n')
                        else:
                            print('parse failed or no message.')
                            print('try next url...')
                        
                        break
                    else:
                        print('no response.')
            except:
                traceback.print_exc()
        
        renpy.invoke_in_thread(fetch_web_notifications)







screen web_notifications():


    zorder 141

    vbox:
        spacing 40

        xoffset -20 yoffset -130
        align 1.0, 1.0

        for i, message in enumerate(web_messages):
            frame:
                xalign 1.0
                background Solid('#00000080')
                has text "[message]"
                if renpy.variant("small"):
                    size gui.huge
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
