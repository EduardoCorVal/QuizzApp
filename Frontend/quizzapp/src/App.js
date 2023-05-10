import "./App.css";
import Register from "./pages/Register";
import Header from "./components/Header";
import Question from "./components/Question";
import Subtitle from "./components/Subtitle";
import Ejemplo from "./images/ejemplo.png"
import LeaderBoard from "./components/LeaderBoard";
import FinalScore from "./pages/FinalScore";


function App() {
  return (
    <div className="App">
      <FinalScore 
      user = "Paulo"
      score = "10"
      user1 = "Jose Luis"
      score1 = "100"
      user2 = "Eduardo"
      score2 = "100"
      user3 = "Angel"
      score3 = "100"
      user4 = "Pablo"
      score4 = "90"
      user5 = "Aleny"
      score5 = "80"
      user6 = "Humbero Alumno"
      score6 = "70"
      user7 = "David"
      score7 = "60"
      user8 = "Christian"
      score8 = "50"
      user9 = "Jorge"
      score9 = "40"
      user10 = "Max"
      score10 = "30"/>
    </div>
  );
}

export default App;
