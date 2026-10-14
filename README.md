# Commit Buddy

A tiny command-line app for saving daily Python learning notes. It is also a starter project for learning GitHub Actions: every push and pull request runs the automated tests.

## Requirements

- Python 3.12 or newer
- No third-party packages

## Run the app

Add a note:

```powershell
python src/app.py --file notes.json add "Learned how unittest discovery works"
```

List saved notes:

```powershell
python src/app.py --file notes.json list
```

The `--file` option chooses where notes are stored. If you leave it out, the app uses `~/.commit_buddy.json` in your home folder.

## Run tests locally

```powershell
python -m unittest discover -s tests -v
```

## Learn GitHub Actions

The workflow in `.github/workflows/ci.yml` runs when you push a commit or open/update a pull request. GitHub starts a fresh runner, checks out the repository, installs Python 3.12, and runs the same `unittest` command shown above. No extra dependency-install step is needed because the app uses only Python's standard library.

To try it, create a GitHub repository, push this project, then open the **Actions** tab. Select the **Python tests** workflow to inspect each step and its output. You can also make a change that breaks a test and push it to see a failed run, then fix the change and push again.
