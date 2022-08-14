import * as React from 'react'

const MusicContext = React.createContext()

function MusicDisplay() {
    const {count} = React.useContext(CountContext)
    return <div>{count}</div>
  }
  