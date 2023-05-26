/* Authors */
// Final Project: Quiz Application with Microservices
// Date: 28-Nov-2022
// Authors:
//          A01746664 Eduardo Joel Cortez Valente
//          A01751587 Paulo Ogando Gulias 
//          A01745865 José Ángel García Gómez 
//          A01745419 José Luis Madrigal Sánchez

import Header from "../components/Header";
import Question from "../components/Question";

import React, { Fragment} from 'react'

function Questions(props) {
  return (
    <Fragment>
      <Header />
      <Question page={props.page} setPage={props.setPage}/>
    </Fragment>
  )
}

export default Questions