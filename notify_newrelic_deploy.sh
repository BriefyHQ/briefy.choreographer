export BRANCH=$1
export REVISION=`git rev-parse $BRANCH`
export CHANGELOG=`git log --oneline -1 $BRANCH`

if [ ${BRANCH} = "master" ]; then
   export APP_ID=42031110
   export APP_KEY=9808689d7c2d3a1afb660b2136d4f15f01275ecc0c8701a
else
   export APP_ID=20678818
   export APP_KEY=c9a9546e2530ea5040e45db4b7e373545ea5462416d6872
fi

curl -X POST "https://api.newrelic.com/v2/applications/${APP_ID}/deployments.json" \
     -H "X-Api-Key:${APP_KEY}" -i \
     -H "Content-Type: application/json" \
     -d \
"{
  \"deployment\": {
   \"revision\": \"${REVISION}\",
    \"changelog\": \"${CHANGELOG}\",
    \"description\": \"briefy.leica deployed from ${BRANCH} branch or tag\",
    \"user\": \"developer@briefy.co\"
  }
}"
