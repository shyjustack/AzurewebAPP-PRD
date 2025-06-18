<!DOCTYPE html>
<html>
<head>
  <title>Quiz</title>
</head>
<body>
  <h2>Quiz: Git Basics</h2>
  <form id="quizForm">
    <p>1. What command initializes a new Git repository?</p>
    <input type="radio" name="q1" value="a"> git start<br>
    <input type="radio" name="q1" value="b"> git init<br>
    <input type="radio" name="q1" value="c"> git new<br>

    <p>2. What does 'git status' show?</p>
    <input type="radio" name="q2" value="a"> Current branch and changes<br>
    <input type="radio" name="q2" value="b"> Commit history<br>
    <input type="radio" name="q2" value="c"> Git version<br>

    <br>
    <input type="submit" value="Submit">
  </form>

  <div id="result"></div>

  <script>
    document.getElementById('quizForm').addEventListener('submit', function(e) {
      e.preventDefault();
      let score = 0;

      if (document.querySelector('input[name="q1"]:checked')?.value === 'b') score++;
      if (document.querySelector('input[name="q2"]:checked')?.value === 'a') score++;

      document.getElementById('result').innerHTML = `You scored ${score}/2`;
    });
  </script>
</body>
</html>
