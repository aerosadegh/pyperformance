# PyPerformance

## 1. Prepare Test Results
```bash
cd docker
docker-compose.yaml up -d
```
Note: This step can take longer than 1 hour.


## 2. Compare Results
If all containers stoped and `docker/results/output` have only `analysis.py` without anything else please run below command:
```bash
docker start docker-compare
```

## 3. Show Result
open Compare.png and speed_up.csv `docker/results/output` directory to show compare results