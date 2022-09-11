import React from 'react';
import RadioIcon from "@mui/icons-material/Radio";

import spotifyIcon from '../../assets/icons/brands/spotify.svg'
import youtubeIcon from '../../assets/icons/brands/youtube.svg'
import tidalIcon from '../../assets/icons/brands/tidal.svg'
import chromeIcon from '../../assets/icons/brands/chrome.svg'
interface BrandIconProps {
  name: string;
}

export const BrandIcon = ({name}: BrandIconProps) => {
  switch (name){
    case 'spotify': 
      return (<img src={spotifyIcon} width={30} />)
    case 'youtube':
      return (
          <img src={youtubeIcon} width={30} />
      );
    case 'tidal':
      return (
          <img src={tidalIcon} width={30} />
      );
    default:
      return name.includes("chromium") ? (<img src={chromeIcon} width={30} />) : (<RadioIcon width={30} fontSize="large" style={{paddingTop: 5}} /> );
  }
}
