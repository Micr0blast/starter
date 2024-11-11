import hello_world

def test_greeting(capsys):
    agent = hello_world.Greeting(greeting="Good day")
    agent.greet("Dr. Klaus")
    out, err = capsys.readouterr()
    assert "Good day, Dr. Klaus!" in out