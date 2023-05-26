/* Authors */
// Final Project: Quiz Application with Microservices
// Date: 28-Nov-2022
// Authors:
//          A01746664 Eduardo Joel Cortez Valente
//          A01751587 Paulo Ogando Gulias 
//          A01745865 José Ángel García Gómez 
//          A01745419 José Luis Madrigal Sánchez

import { createContext, useState } from "react";
import AppContext from "./components/AppContext";

/* Main Style */
import "./App.css";

/* Pages */
import Register from "./pages/Register";
import Questions from "./pages/Questions";
import FinalScore from "./pages/FinalScore";

export const UserContext = createContext();

function App() {
  const [page, setPage] = useState(0);
  const pages = [<Register page={page} setPage={setPage}/>, <Questions page={page} setPage={setPage}/>, <FinalScore page={page} setPage={setPage}/>];

  return (
    <div className="App">
      <AppContext>
        {pages[page]}
      </AppContext>
    </div>
  );
}

export default App;
