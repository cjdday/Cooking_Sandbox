#!/usr/bin/env bash

########################################
# Make the script executable on first run
########################################
if [ ! -x "$0" ]; then
    chmod +x "$0"
fi

set -euo pipefail


########################################
# Load .env variables
########################################
if [ -f .env ]; then
    set -a
    . .env
    set +a
else
    echo "❌ No .env file found."
    exit 1
fi


########################################
# Validate required vars
########################################
REQUIRED_VARS=("DOCKERHUB_USERNAME" "DOCKERHUB_TOKEN" "DOCKERHUB_REPO")
for VAR in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!VAR:-}" ]; then
        echo "❌ Missing required variable in .env: $VAR"
        exit 1
    fi
done

TAG=${DOCKERHUB_TAG:-main}
RUN_FLAGS=${DOCKERHUB_RUN_FLAGS:-}


########################################
# Login to Docker Hub
########################################
echo "🔐 Logging into Docker Hub..."
echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin


########################################
# Fetch the latest DIGEST for this tag
########################################
echo "🔎 Fetching latest digest for: $DOCKERHUB_REPO:$TAG ..."

DIGEST=$(docker buildx imagetools inspect "$DOCKERHUB_REPO:$TAG" \
    | grep "Digest:" \
    | head -n 1 \
    | awk '{print $2}')

if [ -z "$DIGEST" ]; then
    echo "❌ Could not retrieve digest for $DOCKERHUB_REPO:$TAG"
    exit 1
fi

echo "📌 Latest digest found: $DIGEST"


########################################
# Pull the image by digest
########################################
echo "⬇️ Pulling image: $DOCKERHUB_REPO@$DIGEST ..."
docker pull "$DOCKERHUB_REPO@$DIGEST"


########################################
# Run the container
########################################
echo "🚀 Running container from digest..."
echo "➡️  docker run -it --rm $RUN_FLAGS $DOCKERHUB_REPO@$DIGEST"
docker run -it --rm $RUN_FLAGS "$DOCKERHUB_REPO@$DIGEST"
