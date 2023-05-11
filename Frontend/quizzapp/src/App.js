import "./App.css";
import Register from "./pages/Register";
import Header from "./components/Header";
import Question from "./components/Question";
import Subtitle from "./components/Subtitle";
import Ejemplo from "./images/ejemplo.png"
import LeaderBoard from "./components/LeaderBoard";
import FinalScore from "./pages/FinalScore";


function App() {

  const user = 
    {
      name: "Paulo",
      score: 20
    }
  const arrUsers = [
    {
        name: "Jose Luis",
        score: 100
    },
    {
        name: "Angel",
        score: 80
    },
    {
        name: "Eduardo",
        score: 70
    }
  ]
  return (
    <div className="App">
      <FinalScore
      boardUsers = {arrUsers}
      actualUser = {user}/>
    </div>
  );
}

export default App;
