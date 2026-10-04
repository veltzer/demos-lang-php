# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/exercises/Lecture6/ex4_login.php:23` - the login solution builds its SQL by interpolating `$_POST['username']`/`$_POST['password']` straight into the query (classic SQL injection: `' OR '1'='1' -- ` logs in) and stores passwords as unsalted `md5()`. As a model answer this teaches the vulnerability. Use PDO/mysqli prepared statements and `password_hash()`/`password_verify()`.
- `src/exercises/Lecture6/ex4_login.php:21` - `mysql_connect`/`mysql_query`/`mysql_fetch_assoc` (also `src/exercises/Lecture6/ex4_create_table.php:2`-`21`) were removed in PHP 7.0; on the PHP 8.5 in use these scripts die with "Call to undefined function". `php -l` (the `php_lint` processor, `rsconstruct.toml:48`) only checks syntax, so CI stays green. Port to PDO or mysqli.
- `src/exercises/interbit_oren/pdf1/ex09/sol.php:13` - the exercise solutions call `split()`, removed in PHP 7.0 (also `pdf1/ex10/sol.php:13`,`16`, `pdf2/ex1/sol.php:13`, `pdf2/ex2/sol.php:13`, `pdf2/ex3/sol.php:15`,`18`,`26`), so every one of them fatals at run time. Replace with `explode()` (or `preg_split()` where a regex is meant).
- `src/examples/tdd/ArrayTest.php:4` - all PHPUnit demos extend `PHPUnit_Framework_TestCase` (removed in PHPUnit 6), `PHPUnit_Extensions_OutputTestCase` (`OutputTest.php:4`) or `PHPUnit_Extensions_PerformanceTestCase` (`PerformanceTest.php:4`), and use `setExpectedException()` / `@expectedException` (`ExceptionTest.php:6`,`12`, `ExpectedErrorTest.php:6`); none of them loads under any supported PHPUnit, so `src/examples/tdd/Makefile:31` fails. Port to `PHPUnit\Framework\TestCase`, `expectException()`, `expectOutputString()`, and `setUp(): void`; refresh `README.txt`/`exercises.txt` (PHPUnit 3.4 output, PEAR install instructions) to match.

## Medium

- `src/examples/object_oriented/object_realbasic.php:14` - `function Person()` is a PHP 4 style constructor; since PHP 8.0 it is an ordinary method, so `new Person` leaves `name`/`age` null and the demo prints 100 empty `<br/>` pairs (verified with php 8.5). Rename it `__construct()`.
- `scripts/php_lint.py:25` - when the file does not exist this prints `{cmd}`, but `cmd` is only assigned in the usage branch (line 20), so the error path raises `NameError`. The script is also obsolete: `rsconstruct.toml:45`-`48` says the `php_lint` processor replaced it and nothing calls it any more. Delete the script (and the unused `BULLSHIT` constant on line 14 with it).
- `src/exercises/session/showsession.php:7` - echoes `$_SESSION['location']`, which comes unfiltered from `$_POST` (`saveinsession.php:3`), so the session demo is a stored XSS. Wrap the output in `htmlspecialchars()`.

## Low

- `src/exercises/shopping_cart/Utils.php:9` - `trigger_error($msg, E_USER_ERROR)` is deprecated since PHP 8.4 (php 8.5 prints "Passing E_USER_ERROR to trigger_error() is deprecated"). Throw an exception instead and let the page handle it.
- `TODO.txt:2` - "add checking of python scripts" is done (`rsconstruct.toml:27`-`32` run ruff and mypy over `scripts`); move it to `DONE.txt`.
