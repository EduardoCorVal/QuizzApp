/* Authors */
// Final Project: Quiz Application with Microservices
// Date: 28-Nov-2022
// Authors:
//          A01751587 Paulo Ogando Gulias

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