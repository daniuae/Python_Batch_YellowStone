# Java Advanced APIs -- Study Guide

> This is a concise Markdown edition covering the requested topics.

## 1. Collections API Deep Dive

### Collection Hierarchy

``` text
Iterable
 └── Collection
      ├── List
      ├── Set
      └── Queue

Map (Separate Interface)
```

### Common Collections

  Interface   Implementation      Ordered   Duplicate   Thread Safe
  ----------- ------------------- --------- ----------- -------------
  List        ArrayList           Yes       Yes         No
  List        LinkedList          Yes       Yes         No
  Set         HashSet             No        No          No
  Set         TreeSet             Sorted    No          No
  Map         HashMap             No        Keys No     No
  Map         ConcurrentHashMap   No        Keys No     Yes

## 2. Streams API

``` java
List<Integer> numbers = List.of(2,5,8,10);

numbers.stream()
       .filter(n -> n % 2 == 0)
       .map(n -> n * n)
       .forEach(System.out::println);
```

### Collectors

``` java
List<Integer> even = numbers.stream()
    .filter(n -> n % 2 == 0)
    .toList();
```

``` java
Map<Boolean,List<Integer>> grouped =
numbers.stream()
.collect(Collectors.partitioningBy(n -> n % 2 == 0));
```

## 3. Date & Time API

``` java
LocalDate today = LocalDate.now();
LocalDateTime now = LocalDateTime.now();
ZonedDateTime india =
    ZonedDateTime.now(ZoneId.of("Asia/Kolkata"));
```

## 4. HTTP Client API

``` java
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com"))
    .build();

HttpResponse<String> response =
client.send(request, HttpResponse.BodyHandlers.ofString());
```

## 5. Regular Expressions

``` java
Pattern p = Pattern.compile("\\d+");
Matcher m = p.matcher("Age 35");

while(m.find()){
    System.out.println(m.group());
}
```

## 6. JDBC Architecture

``` text
Application
   ↓
JDBC API
   ↓
DriverManager
   ↓
Driver
   ↓
Database
```

### CRUD

``` java
PreparedStatement ps =
con.prepareStatement(
"INSERT INTO Employee VALUES(?,?,?)");
```

### Transactions

``` java
con.setAutoCommit(false);

try{
    // SQL operations
    con.commit();
}catch(Exception e){
    con.rollback();
}
```

### CallableStatement

``` java
CallableStatement cs =
con.prepareCall("{call GetEmployee(?)}");
```

## 7. CompletableFuture

``` java
CompletableFuture.supplyAsync(() -> 10)
.thenApply(n -> n * 5)
.thenAccept(System.out::println);
```

## 8. Concurrent Collections

### ConcurrentHashMap

``` java
ConcurrentHashMap<Integer,String> map =
new ConcurrentHashMap<>();
```

### CopyOnWriteArrayList

``` java
CopyOnWriteArrayList<String> list =
new CopyOnWriteArrayList<>();
```

## 9. HikariCP

### Maven

``` xml
<dependency>
    <groupId>com.zaxxer</groupId>
    <artifactId>HikariCP</artifactId>
    <version>6.2.1</version>
</dependency>
```

### Configuration

``` java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:mysql://localhost:3306/company");
config.setUsername("root");
config.setPassword("password");

HikariDataSource ds =
new HikariDataSource(config);
```

## Best Practices

-   Use PreparedStatement.
-   Prefer try-with-resources.
-   Use java.time instead of Date.
-   Use connection pooling in production.
-   Keep transactions short.
-   Use concurrent collections only when needed.

## Interview Questions

1.  Difference between HashMap and ConcurrentHashMap?
2.  map() vs flatMap()?
3.  Why PreparedStatement?
4.  What is CompletableFuture?
5.  Why HikariCP?
