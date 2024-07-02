# Privacera Platform deployment size  
  
<table>  
<tr>  
<th>

Pod

</th>  
<th>

Small

</th>  
<th>

Medium

</th>  
<th>

Large

</th></tr>  
<tr>  
<td>

</td>  
<td>

Memory

</td>  
<td>

CPU

</td>  
<td>

Disk

</td>  
<td>

Replication Factor

</td>  
<td>

Memory

</td>  
<td>

CPU

</td>  
<td>

Disk

</td>  
<td>

Replication Factor

</td>  
<td>

Memory

</td>  
<td>

CPU

</td>  
<td>

Disk

</td>  
<td>

Replication Factor

</td></tr>  
<tr>  
<td>

Portal

</td>  
<td>

2GB

</td>  
<td>

0.5

</td>  
<td>

NA

</td>  
<td>

min=1 max=1

</td>  
<td>

4G

</td>  
<td>

2

</td>  
<td>

NA

</td>  
<td>

</td>  
<td>

8G

</td>  
<td>

4

</td>  
<td>

NA

</td>  
<td>

</td></tr>  
<tr>  
<td>

Maria DB

</td>  
<td>

1GB

</td>  
<td>

0.5

</td>  
<td>

12

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

12

</td>  
<td>

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

12

</td>  
<td>

</td></tr>  
<tr>  
<td>

Data Server

</td>  
<td>

2GB

</td>  
<td>

1

</td>  
<td>

NA

</td>  
<td>

min=1 max=1

</td>  
<td>

8GB

</td>  
<td>

2

</td>  
<td>

NA

</td>  
<td>

min=2 max=4

</td>  
<td>

8GB

</td>  
<td>

2

</td>  
<td>

NA

</td>  
<td>

min=3 max=20

</td></tr>  
<tr>  
<td>

Discovery - Driver

</td>  
<td>

2GB

</td>  
<td>

1

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

16GB

</td>  
<td>

8

</td>  
<td>

32

</td>  
<td>

</td></tr>  
<tr>  
<td>

Discovery - Executor

</td>  
<td>

2GB

</td>  
<td>

1

</td>  
<td>

NA

</td>  
<td>

</td>  
<td>

2GB

</td>  
<td>

2

</td>  
<td>

NA

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

4

</td>  
<td>

NA

</td>  
<td>

</td></tr>  
<tr>  
<td>

PolicySync

</td>  
<td>

2GB

</td>  
<td>

2

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

32GB

</td>  
<td>

8

</td>  
<td>

32

</td>  
<td>

</td></tr>  
<tr>  
<td>

Solr

</td>  
<td>

1.5GB

</td>  
<td>

1

</td>  
<td>

64

</td>  
<td>

1

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

64

</td>  
<td>

3

</td>  
<td>

32GB

</td>  
<td>

8

</td>  
<td>

64

</td>  
<td>

3

</td></tr>  
<tr>  
<td>

Zookeeper

</td>  
<td>

1GB

</td>  
<td>

0.5

</td>  
<td>

32

</td>  
<td>

1

</td>  
<td>

2GB

</td>  
<td>

1

</td>  
<td>

32

</td>  
<td>

3

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

32

</td>  
<td>

3

</td></tr>  
<tr>  
<td>

Atlas

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td></tr>  
<tr>  
<td>

Ranger KMS

</td>  
<td>

1GB

</td>  
<td>

0.5

</td>  
<td>

12 NA

</td>  
<td>

</td>  
<td>

2GB

</td>  
<td>

2

</td>  
<td>

12 NA

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

4

</td>  
<td>

12 NA

</td>  
<td>

</td></tr>  
<tr>  
<td>

Ranger UserSync

</td>  
<td>

1GB

</td>  
<td>

0.5

</td>  
<td>

12 NA

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

12 NA

</td>  
<td>

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

12 NA

</td>  
<td>

</td></tr>  
<tr>  
<td>

Grafana

</td>  
<td>

1GB

</td>  
<td>

0.5

</td>  
<td>

1

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

1

</td>  
<td>

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

1

</td>  
<td>

</td></tr>  
<tr>  
<td>

Graphite

</td>  
<td>

1GB

</td>  
<td>

0.5

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

32

</td>  
<td>

</td></tr>  
<tr>  
<td>

Kafka

</td>  
<td>

1GB

</td>  
<td>

0.5

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

32

</td>  
<td>

</td></tr>  
<tr>  
<td>

PEG

</td>  
<td>

1GB

</td>  
<td>

0.5

</td>  
<td>

NA

</td>  
<td>

min=1 max=2

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

NA

</td>  
<td>

min=2 max=10

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

NA

</td>  
<td>

min=3 max=20

</td></tr>  
<tr>  
<td>

pkafka

</td>  
<td>

1GB

</td>  
<td>

0.5

</td>  
<td>

NA

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

NA

</td>  
<td>

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

NA

</td>  
<td>

</td></tr>  
<tr>  
<td>

Ranger Admin

</td>  
<td>

2GB

</td>  
<td>

1

</td>  
<td>

NA

</td>  
<td>

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

NA

</td>  
<td>

min=2 max=4

</td>  
<td>

16GB

</td>  
<td>

8

</td>  
<td>

NA

</td>  
<td>

min=2 max=4

</td></tr>  
<tr>  
<td>

Flowable

</td>  
<td>

1GB

</td>  
<td>

0.5

</td>  
<td>

NA

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

NA

</td>  
<td>

</td>  
<td>

8GB

</td>  
<td>

4

</td>  
<td>

NA

</td>  
<td>

</td></tr>  
<tr>  
<td>

Audit Server

</td>  
<td>

1GB

</td>  
<td>

1

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

16GB

</td>  
<td>

8

</td>  
<td>

32

</td>  
<td>

</td></tr>  
<tr>  
<td>

FluentD

</td>  
<td>

1GB

</td>  
<td>

1

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

4GB

</td>  
<td>

2

</td>  
<td>

32

</td>  
<td>

</td>  
<td>

16GB

</td>  
<td>

8

</td>  
<td>

32

</td>  
<td>

</td></tr>  
<tr>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td></tr>  
<tr>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

289

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

289

</td>  
<td>

</td>  
<td>

</td>  
<td>

</td>  
<td>

289

</td>  
<td>

</td></tr></table>



<div class="grid cards" markdown>
-   :material-page-previous: [Prev](privacera-platform-installation-overview.md)
-   :material-page-next: [Next](privacera-platform-installation-prerequisites.md)
</div>
