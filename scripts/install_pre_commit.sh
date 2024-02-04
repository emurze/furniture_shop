#!/bin/sh

set -e

git init

touch .git/hooks/pre-commit

chmod +x .git/hooks/pre-commit

echo '''
#!/bin/sh
bash scripts/pre_commit.sh
''' > .git/hooks/pre-commit