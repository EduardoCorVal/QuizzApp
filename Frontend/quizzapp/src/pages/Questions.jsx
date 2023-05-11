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