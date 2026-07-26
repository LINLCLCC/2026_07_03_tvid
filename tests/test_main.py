from main import main


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from 2026-07-03-tvid!" in captured.out
