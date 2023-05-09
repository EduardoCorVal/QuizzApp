import React from 'react'
import '../styles/Subtitle.css'

function Subtitle(props){
  return (
    <div className='subtitle'>
        <p className='subtitle-text'>{props.text}</p>
    </div>
  )
}

export default Subtitle