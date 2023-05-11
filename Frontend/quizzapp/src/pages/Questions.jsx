import Header from "../components/Header";
import Question from "../components/Question";

import React, { Fragment, useContext } from 'react'
import { UserContext } from '../App'


function Questions() {
  return (
    <Fragment>
      <Header />
      <Question />
    </Fragment>
  )
}

export default Questions