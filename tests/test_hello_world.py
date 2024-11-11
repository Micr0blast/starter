import hello_world

def test_greeting(capsys):
    agent = hello_world.Greeting(greeting="Good day")
    agent.greet("Dr. Klaus")
    out, err = capsys.readouterr()
    assert out is "Good day, Dr. Klaus!"