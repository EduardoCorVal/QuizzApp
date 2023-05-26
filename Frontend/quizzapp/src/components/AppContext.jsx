/* Authors */
// Final Project: Quiz Application with Microservices
// Date: 28-Nov-2022
// Authors:
//          A01745865 José Ángel García Gómez 

import React, {Children, useState} from 'react';
import { UserContext } from '../App';

function AppContext({children}) {
    const [user, setUser] = useState();
    const [questions, setQuestions] = useState();
    const [score, setScore] = useState(0);
  return (
    <UserContext.Provider value={[user, setUser, questions, setQuestions, score, setScore]}>
        {children}
    </UserContext.Provider>
  )
}

export default AppContext