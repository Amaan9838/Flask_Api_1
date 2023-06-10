import logging
from typing import Any, Callable, Dict, List, Optional

import pytube
import pytube.exceptions as exceptions
from pytube import extract, request
from pytube import Stream, StreamQuery
from pytube.helpers import install_proxy
from pytube.innertube import InnerTube
from pytube.metadata import YouTubeMetadata
from pytube.monostate import Monostate
from pytube import YouTube

class CustomYouTube(YouTube):
    def bypass_age_gate(self):
        # Custom implementation for bypass_age_gate
        # Add your code here
         innertube = InnerTube(
            client='ANDROID',
            use_oauth=self.use_oauth,
            allow_cache=self.allow_oauth_cache
        )
         innertube_response = innertube.player(self.video_id)

         playability_status = innertube_response['playabilityStatus'].get('status', None)

        # If we still can't access the video, raise an exception
        # (tier 3 age restriction)
         if playability_status == 'UNPLAYABLE':
            raise exceptions.AgeRestrictedError(self.video_id)

         self._vid_info = innertube_response
         pass
