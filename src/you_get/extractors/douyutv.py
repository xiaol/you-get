#!/usr/bin/env python

__all__ = ['douyutv_download']

from ..common import *
import json

def douyutv_download(url, output_dir = '.', merge = True, info_only = False):
# <<<<<<< HEAD
#     html = get_html(url)
#     room_id_patt = r'"room_id":(\d{1,99}),'
#     title_patt = r'<div class="headline clearfix">\s*<h1>([^<]{1,9999})</h1>\s*</div>'
#
#     roomid = re.findall(room_id_patt,html)[0]
#     title = unescape_html(re.findall(title_patt,html)[0])
# =======
    room_id = url[url.rfind('/')+1:]
# >>>>>>> 1b55b01b047824312c2eba342eed47d1d0503a97

    content = get_html("http://www.douyutv.com/api/client/room/"+room_id)
    data = json.loads(content)['data']

    title = data.get('room_name')
    real_url = data.get('rtmp_url')+'/'+data.get('rtmp_live')

    print_info(site_info, title, 'flv', float('inf'))
    if not info_only:
        download_urls([real_url], title, 'flv', None, output_dir, merge = merge)

site_info = "douyutv.com"
download = douyutv_download
download_playlist = playlist_not_supported('douyutv')
