# สรุปสอบ Flutter — ตามใบ Lab ทั้งหมด (เอกสารคนเดียวพกเข้าห้องสอบได้)

> รูปแบบสอบตามที่ อ.สิทธิ ประกาศ: **ทำตามใบ Lab · รวมเป็น 1 โปรแกรม · เอาเอกสารเข้าฟ้องได้ · ทำเสร็จ → ตรวจข้อสอบ → ถาม-ตอบ ปากเปล่า**
> วิชา: Advanced Mobile Programming (Flutter/Dart) · สอบวันอังคาร

---

## 0. คำสั่งที่ใช้บ่อย (Terminal ในโฟลเดอร์โปรเจค)

| คำสั่ง | ทำอะไร |
|---|---|
| `flutter doctor` | เช็ก environment ว่าพร้อมไหม |
| `flutter create my_app` | สร้างโปรเจค — **ชื่อต้องเป็นตัวเล็กทั้งหมด ใช้ `_` ขีดกลางไม่ได้** เช่น `Hello_1` → error |
| `flutter run` / กด `F5` | รันไปที่ AVD |
| `flutter pub get` | ติดตั้งแพ็กเกจจาก pubspec (ถ้ากด Save แล้วไม่โหลด) |
| `flutter pub add http` | เพิ่มแพ็กเกจ http |
| `flutter upgrade` / `flutter packages get` / `flutter analyze` / `flutter format` | อัปเดต SDK / แพ็กเกจ / ตรวจโค้ด / จัดโค้ด |
| `dart --enable-asserts file.dart` | รันไฟล์ที่มี `assert` |
| Hot Reload (สายฟ้า) | inject โค้ดใหม่เข้า VM — **state ไม่หาย** |

สร้างโปรเจคใน VS Code: `Ctrl+Shift+P` → `Flutter: New Project` → `Application` → เลือกโฟลเดอร์ → ตั้งชื่อ (ตัวเล็ก-ขีดล่าง)

⚠️ แก้ชื่อคลาสหลักแล้ว **อย่าลืมแก้ `test/widget_test.dart`** ให้ตรงด้วย ไม่งั้น test ฟาว

---

## 1. Dart พื้นฐาน (Lab 02)

```dart
void main() {
  print('hello world');   // ทุกคำสั่งต้องลง ; เสมอ
}
```

**ชนิดข้อมูล**

| type | ตัวอย่าง |
|---|---|
| `int` | 0, 1, -5 |
| `double` | 0.0, -12.34 |
| `num` | ทั้ง int และ double |
| `bool` | true, false |
| `String` | `'hi'` หรือ `"hi"` (ใช้ได้ทั้งคู่) |
| `dynamic` | เปลี่ยนชนิดได้ตลอด |
| `List` | array → `[1,2,3]` |
| `Map` | json-like → `{'code':'007'}` |

**var / final / const / dynamic**

- `var` → ชนิดถูกกำหนดจากค่าครั้งแรก แล้วเปลี่ยนไม่ได้ (`var y = 10;` แล้ว `y='x';` → **Error**)
- `dynamic` → เปลี่ยนชนิดได้ตลอด แต่เสี่ยง runtime error
- `final` → กำหนดค่าตอน **runtime** ห้ามเปลี่ยนภายหลัง (ค่าอาจมาจากฟังก์ชัน/ตัวแปรอื่น)
- `const` → ค่าคงที่ตอน **compile-time** ต้องเป็น literal (เช่น `10`, `'value'`)

**เครื่องหมายคำนวณ** `+ - * / %`
- ⚠️ `int / int` ได้ **double** (ต่างจาก C) → `int a = 2/2;` = error
- แก้: `4 ~/ 2` (หารปัดทิ้ง) หรือ `(4/2).toInt()`

**String**
```dart
print('a = ' + a.toString());   // + ต่อสตริง ต้อง toString ก่อน
print('a is $a');                // interpolation
print('a + b = ${a + b}');       // expression ต้องครอบ ${ }
String c = '''multi
line''';                          // หลายบรรทัด
```

**Null Safety**
- ค่าเริ่มต้นเป็น **non-nullable** → ใส่ `?` ถ้าต้องการให้เป็น null ได้: `int? x;`
- `??` Null Coalescing: `x ?? 1` → ถ้า null ใช้ค่า 1
- `?.` Null Conditional: `people?.sayHi()` → ถ้าไม่ null ค่อยเรียก
- `!` ยืนยันว่าไม่เป็น null แน่ ๆ (เสี่ยง error ถ้าเป็น null)
- แปลงชนิด: `int.parse('10')`, `double.parse('10.5')`, `a.toString()`

**List / Map**
```dart
List data = [1,2,3,4];
print(list[0]);  print(data.elementAt(0));
data.add(x); data.remove(x); data.removeAt(0);
print(obj.first); print(obj.last);

var data = {'code':'007'};   // Map<String,String>
print(data['code']);
data['code2'] = '008';
```

**OOP 3 อย่างของ object** (ตามสไลด์): State / Behavior / Identity · Class = blueprint · Method = การสื่อสารระหว่าง object

---

## 2. Control Flow (Lab 03-1)

```dart
if (x > 5) {...} else if (...) {...} else {...}

// Ternary (if-else ลดรูป)
var r = cond ? exp1 : exp2;
// ถ้า exp1 เป็น null ใช้ exp2
var r2 = exp1 ??= exp2;

for (int i = 0; i < 5; i++) { print('RMUTT ${i+1}'); }

var obj = [1,2,3,4,5];
for (var p in obj) { print(p); }      // for-in

while (cond) {...}
do {...} while (cond);                // อย่างน้อย 1 รอบ
break; continue;

switch (n) {                          // Dart ใช้ได้กับ int
  case 1: print('one'); break;
  default: print('other');
}

assert(status == 4, 'status must be 4');  // false = throw + หยุด (โหมด dev เท่านั้น)
```

**เมธอดของ List ที่ออกข้อสอบบ่อย**

```dart
var obj = [1,4,8,10,15];
obj.firstWhere((e) => e >= 9);     // 10   (ตัวแรกที่เข้าเงื่อนไข)
obj.lastWhere((e) => e > 9);       // 15
obj.where((e) => e.endsWith('t')); // กรอง คืนเป็น Iterable

var s = ['dart','test','thailand'];
s.firstWhere((e) => e.startsWith('t'));   // 'dart'
s.lastWhere((e) => e.endsWith('t'));      // 'thailand'

List.generate(6, (index) => 'RMUTT-${index+1}');   // generator
obj.forEach((e) => print(e));

// Set = ค่าซ้ำกันไม่ได้ (unique)
```

**Function**
```dart
int fib(int n) => n <= 1 ? n : fib(n-1) + fib(n-2);   // arrow function

void hello() => print('Hello');          // 1 คำสั่ง ไม่ต้องมี return / {}

int add(int a, [int b = 0]) => a + b;    // optional parameter (ค่าเริ่มต้น)

int inc(int x) { return x + 1; }         // ฟังก์ชันปกติ
```

**Class สร้าง object**: `var std1 = Student();` หรือ `new Student();` แล้ว `std1.name='Somchai'; std1.hello();`
มี **Callable Class** (class ที่มี `call()` เรียกเหมือนฟังก์ชัน)

---

## 3. OOP: Class & Inheritance (Lab 04-1)

**4 หลัก OOP**: Encapsulation · Inheritance · Polymorphism · Abstraction

```dart
class Car {
  int color;
  String model;
  void display() => print('This Model is $model');
}
var car1 = Car();
car1.model = 'Yaris';
car1.display();
```

- **`this`** = ตัว object เอง ใช้ตอนชื่อตัวแปรซ้ำกับ parameter (`this.model = model;`)
- **private**: ขึ้นต้นด้วย `_` → `_privateField`, `_privateMethod()` (เข้าถึงได้ในไฟล์เดียวกัน)
- **Getter/Setter** ใช้เข้า property ที่เป็น private:
```dart
class Car {
  String _model;
  String get model => _model;
  set model(String model) => _model = model;
}
car1.model = 'City';   // เรียก setter
var a = car1.model;    // เรียก getter
```
- **Constructor**: `Car(this._color, this._model);`
  ถ้าเป็น `final` ต้องใช้ initializer: `Car({int color, String model}) : this._color = color, this._model = model;`
- **`==` กับ Object ที่เก็บแบบ reference** → override `operator ==` เอง (หรือเขียน `equals()`) ถ้าอยากเทียบค่าข้างใน:
```dart
@override
bool operator ==(dynamic other) {
  if (other is! Person) return false;
  return other.id == id && other.name == name;
}
```

**Inheritance**
```dart
class B {}                 // SUPER / BASE / PARENT
class A extends B {}       // SUB / CHILD

class Car1 extends Car {
  Car1(int id, String model) : super(id, model);   // เรียก constructor แม่
  @override
  void display() { print(id); print(super.display()); }  // override + super
}
```

**Implement (Interface)** — Dart ไม่มี keyword `interface` ทุก class เป็น interface ได้
```dart
abstract class Shape {
  double width, height;
  void area();             // abstract method
  void perimeter();
}
class Rectangle implements Shape {
  @override double area() => width * height;
  @override double perimeter() => (width*2) + (height*2);
}
// implement แล้วต้องเขียน properties/method ครบทุกตัว ไม่งั้น error
```

**Mixin** — `extends` หลายคลาสด้วย `with` (parent ห้าม extends จาก class อื่น)
```dart
class A with B, C {}
A().test();   // เรียกจากคลาสด้าน "ขวาสุด" = C
```

---

## 4. โครงสร้างแอป + TextStyle (Lab 03-2)

โครงไฟล์ `main.dart` ขั้นต่ำ (ตามใบ Lab — ลบทุกคลาส เหลือแต่ `main`):

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());                 // //1
}

class MyApp extends StatelessWidget {   // คลาส 1: โครงสร้าง App
  const MyApp({super.key});              // Constructor ใส่ {super.key} ทุกครั้ง

  @override
  Widget build(BuildContext context) {   // //2
    return const MaterialApp(
      home: Text('Hello World RMUTT'),
    );                                   // ; ปิดวงเล็บ ใส่ const ให้ถูกที่
  }
}
```

**TextStyle**
```dart
const Text(
  'Hello World RMUTT',
  style: TextStyle(
    color: Colors.red,
    fontSize: 30,
    fontWeight: FontWeight.bold,
    fontStyle: FontStyle.italic,
    fontFamily: 'Tahoma',
  ),
)
```
> หลักการใส่ `const`: ใส่หน้า widget ที่ **ไม่มีตัวแปรเปลี่ยนแปลง** (VS Code จะขึ้นดวงไฟเหลืองให้กด — ถ้ามีค่าเปลี่ยนต้อง **ลบ** const ออก)

**ลำดับ widget (wrap)**: `App → MaterialApp → Scaffold → AppBar / Body` — การสร้าง UI คือการ "ห่อหุ้ม" (wrap) กันเป็นชั้น

---

## 5. Scaffold + StatefulWidget (Lab 05)

```dart
Scaffold(
  appBar: AppBar(title: Text('...')),
  body: ...,                    // Column / Row / Center
  floatingActionButton: ...,
)
```

- `Column(...)` = เรียงแนวตั้ง, `Row(...)` = แนวนอน, `SizedBox(height: 20)` / `SizedBox(width: 20)` = ช่องว่างคั่น
- **Arrow Function**:
```dart
void hello() { print('Hello World'); }
void hello() => print('Hello World');
int inc_num(int x) { return x+1; }
int inc_num(int x) => x+1;      // ไม่ต้องมี return
```

**Pattern StatefulWidget 3 คลาส (จำให้ขึ้นใจ — ออกบ่อย)**

| คลาส | สืบทอด | หน้าที่ |
|---|---|---|
| 1. `MyApp` | `StatelessWidget` | โครงสร้าง App |
| 2. `HomePage` | `StatefulWidget` | หน้าจอที่มีข้อมูลเปลี่ยน → **ต้อง override `createState()`** |
| 3. `HomePageState` | `State<HomePage>` (generic) | UI จริง + ตัวแปรสถานะ + `setState` |

```dart
class HomePage extends StatefulWidget {
  const HomePage({super.key});
  @override
  State<HomePage> createState() => HomePageState();   // arrow function
}

class HomePageState extends State<HomePage> {
  String str = 'Hello';          // ตัวแปรสถานะ

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('App02')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,   // จัดกึ่งกลาง
          children: [
            Text(str),
            const SizedBox(height: 20),
            TextButton(
              onPressed: () {
                setState(() => str = 'สวัสดี');   // สำคัญมาก!
              },
              child: const Text('เปลี่ยนข้อความ'),
            ),
          ],
        ),
      ),
    );
  }
}
```

**`setState` สำคัญแค่ไหน** → ถ้าเปลี่ยนค่าตัวแปรโดยไม่เรียก `setState` UI จะ **ไม่อัปเดต** เพราะ Flutter ไม่รู้ว่ามีอะไรเปลี่ยน
ตัวอย่างแอปบวกเลข/นับจำนวน: ตัวแปร `_value` + ปุ่ม `onPressed: () { setState(() => _value++); }`

---

## 6. Tab Menu + SingleChildScrollView (Lab 04-2)

```dart
return MaterialApp(
  home: DefaultTabController(
    length: 3,                       // จำนวน Tab
    child: Scaffold(
      appBar: AppBar(
        title: const Text('My App'),
        bottom: TabBar(
          tabs: [
            Tab(icon: const Icon(Icons.home),     text: 'หน้าแรก'),
            Tab(icon: const Icon(Icons.person),   text: 'ประวัติ'),
            Tab(icon: const Icon(Icons.settings), text: 'ตั้งค่า'),
          ],
        ),
      ),
      body: TabBarView(
        children: [
          MyHome(),                 // เรียกคลาสจากไฟล์อื่น
          const Icon(Icons.star),
          const Icon(Icons.settings),
        ],
      ),
    ),
  ),
);
```
> ดูรูปไอคอน: https://api.flutter.dev/flutter/material/Icons-class.html

**แยกไฟล์**: คลิกขวา `lib` → New File → `myhome.dart` → ในนั้น import `package:flutter/material.dart` แล้วสร้างคลาส `MyHome extends StatelessWidget` + `{super.key}` + `build()` → ที่ `main.dart` import ไฟล์ (`import 'myhome.dart';`) เรียก `MyHome()`

**SingleChildScrollView**
```dart
// ใน myhome.dart
return const SingleChildScrollView(
  child: Column(
    children: [
      Image.asset('assets/images/pic1.jpg'),
      Text(
        'สาขาวิชาวิศวกรรมคอมพิวเตอร์\nมหาวิทยาลัยเทคโนโลยีราชมงคลธัญบุรี',
        style: TextStyle(fontSize: 20, fontFamily: 'tahoma'),
        textAlign: TextAlign.center,
      ),
      Image.asset('assets/images/pic2.jpg'),
    ],
  ),
);
```

**ขั้นตอน assets (สำคัญ ถ้าพลาดรูปไม่ขึ้น)**
1. สร้างโฟลเดอร์ `assets/images` แล้วลบรูปเข้าไป
2. เปิด `pubspec.yaml` → หาคอมเมนต์ `assets:` → **ยกเลิกคอมเมนต์** แล้วเว้นวรรค/เยื้องให้ถูก:
```yaml
flutter:
  uses-material-design: true
  assets:
    - assets/images/
```
3. `flutter pub get` ถ้าจำเป็น → เรียก `Image.asset('assets/images/ชื่อไฟล์.jpg')`

**การบ้าน ครั้งที่ 1 (โจทย์ที่คล้ายข้อสอบมาก):** แสดงประวัตินักศึกษา **อย่างน้อย 5 ด้าน** ด้วย **TabMenu** ข้อมูล/รูปภาพเลื่อนดูด้วย **SingleChildScrollView**

---

## 7. วิดเจ็ตพื้นฐาน (Lab 06)

**Text**
```dart
Text(
  'ข้อความ',
  textScaleFactor: 1.3,          // ตัวคูณขนาดฟอนต์
  maxLines: 2,                   // จำนวนบรรทัดสูงสุด
  overflow: TextOverflow.clip,    // ตัดคำที่เกิน
  style: TextStyle(color: Colors.red, fontSize: 16,
                   fontWeight: FontWeight.bold, fontStyle: FontStyle.italic,
                   fontFamily: 'Tahoma'),
)
```

**3 ปุ่ม**
| ปุ่ม | ลักษณะ |
|---|---|
| `TextButton` | แบบข้อความ |
| `ElevatedButton` | แบบยกนูน |
| `OutlinedButton` | มีเส้นขอบล้อมรอบ |

```dart
TextButton(
  onPressed: () {},              // ตอบสนองเมื่อกด
  onLongPressed: () {},          // กดค้าง
  child: const Text('กดฉัน'),
)

ElevatedButton(
  onPressed: () {},
  child: const Text('OK'),
  style: ElevatedButton.styleFrom(
    backgroundColor: Colors.green,     // สีพื้น
    foregroundColor: Colors.blue,      // สีตัวอักษร
    shadowColor: Colors.black12,
    side: const BorderSide(color: Colors.red, width: 2),
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
    // shape: const StadiumBorder(),   // มุมโค้ง
  ),
)
```

**TextField (รับค่า)**
```dart
// ตัวแปรคุม TextField
final varCtrlEmail = TextEditingController();

TextField(
  controller: varCtrlEmail,               // เชื่อมกับตัวแปร
  decoration: InputDecoration(
    labelText: 'E-mail',
    border: const OutlineInputBorder(),   // ขอบสี่เหลี่ยม
    prefixIcon: const Icon(Icons.email),
  ),
  style: const TextStyle(fontSize: 18, color: Colors.blue),   // textStyle()
  onChanged: (v) => setState(() => varEmail = v),             // อัปเดตค่า
)
// ใช้เสร็จควร varCtrlEmail.dispose();
```

**FloatingActionButton** — อยู่ใน `Scaffold` ระดับเดียวกับ `appBar`
```dart
floatingActionButton: FloatingActionButton(
  onPressed: () {},
  child: const Icon(Icons.add),
)
```

**Date Time Picker** — ไปที่ https://pub.dev ค้นหาแพ็กเกจ → copy โค้ด `version:` ใส่ใต้ `dependencies:` ใน `pubspec.yaml` (ระวังการเยื้อง/แท็บ) → `flutter pub get` → เรียกใช้ในโค้ด

**Padding**: `body: Padding(padding: EdgeInsets.all(16), child: ...)` (ถ้าใส่ const ที่ `Center` ให้เอาออกก่อนถ้ามีค่าเปลี่ยน)

---

## 8. Login + PHP/MySQL (Lab 08)

**ฝั่งเซิร์ฟเวอร์ (XAMPP)**
1. ติดตั้ง XAMPP → Start **Apache** + **MySQL** (phpMyAdmin: `localhost:81`)
2. สร้าง DB ชื่อ `flutter_mydb` → ตาราง `users` (4 attributes: id, name, email, password)
3. สร้างโฟลเดอร์ `htdocs/login_php` ใส่ไฟล์ PHP:

```php
// connect.php
<?php
$db_name = "flutter_mydb"; $db_user = "root"; $db_pass = ""; $db_host = "localhost";
$con = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
if ($con->connect_error) { die("Connection failed: " . $con->connect_error); }
?>

// register.php  (ทดสอบ: http://127.0.0.1:81/login_php/register.php ต้องได้ "Succeed")
<?php
require "connect.php";
$name = $_POST['name']; $password = $_POST['password']; $email = $_POST['email'];
$encrypted_pwd = md5($password);
$sql = "SELECT * FROM users WHERE email = '$email'";
$result = mysqli_query($con, $sql);
if (mysqli_num_rows($result) == 1) { echo json_encode('Error'); }
else {
  $insert = "INSERT INTO users(name,password,email) VALUES('$name','$encrypted_pwd','$email')";
  if (mysqli_query($con, $insert)) { echo json_encode('Succeed'); }
}
?>

// login.php
<?php
require "connect.php";
$email = $_POST['email']; $password = $_POST['password'];
$encrypted_pwd = md5($password);
$sql = "SELECT * FROM users WHERE email = '$email' AND password = '$encrypted_pwd'";
$result = mysqli_query($con, $sql);
echo json_encode(mysqli_num_rows($result) == 1 ? "Success" : "Error");
?>
```

**ฝั่ง Flutter** — 2 ไฟล์: `main.dart` (Stateless, `home: LoginPage()`, `theme: ThemeData.dark()`) + `login_page.dart` (StatefulWidget)

```dart
class LoginPage extends StatefulWidget {
  const LoginPage({super.key});
  @override
  State<LoginPage> createState() => _LoginPage();      // คลาส private
}

class _LoginPage extends State<LoginPage> {
  final _formKey = GlobalKey<FormState>();             // คุมฟอร์ม
  final _userController = TextEditingController();     // คุม TextField
  final _passController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Login')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,   // หน้า login กลางจอ
            children: [
              Image.network('https://www.rmutt.ac.th/.../logo.png', width: 200),
              TextFormField(
                controller: _userController,
                decoration: const InputDecoration(labelText: 'Username',
                                                   border: OutlineInputBorder()),
                validator: (value) =>
                    (value == null || value.isEmpty) ? 'กรุณาใส่ username' : null,
              ),
              TextFormField(
                controller: _passController,
                obscureText: true,                     // ซ่อนรหัสผ่าน
                decoration: const InputDecoration(labelText: 'Password'),
                validator: (value) =>
                    (value == null || value.isEmpty) ? 'กรุณาใส่ password' : null,
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: () {
                  if (_formKey.currentState!.validate()) {   // ผ่าน validator ทุกช่อง
                    // ยิง http หรือ navigate ต่อ
                  }
                },
                child: const Text('Login'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

**Navigator ไปหน้าถัดไป**
```dart
Navigator(
  onGenerateRoute: (settings) {
    return MaterialPageRoute(builder: (context) => const HomePage());
  },
)
// หรือแบบสั้น
Navigator.push(context, MaterialPageRoute(builder: (context) => const HomePage()));
```

**ยิง API สมัครสมาชิก (async + http)**
```dart
import 'package:http/http.dart' as http;
import 'dart:async';

Future<void> sign_up(String name, String email, String password) async {
  final url = Uri.parse('http://10.0.2.2:81/login_php/register.php');  // AVD → localhost ของเครื่อง
  final response = await http.post(url, body: {
    'name': name, 'email': email, 'password': password,
  });
  // response.body == "Succeed"
}
// ติดตั้ง: flutter pub add http
```
> ข้อควรระวัง: ปุ่มสมัครต้องเช็ก `_formKey.currentState!.validate()` ก่อน ค่อยเรียก `sign_up()`

---

## 9. 🔴 "รวมเป็น 1 โปรแกรม" — โครงที่น่าจะเป็นข้อสอบ

ข้อความที่ อ. ประกาศ: *ตามใบ Lab · แต่รวมเป็น 1 โปรแกรม* → ให้เตรียม สkeleton ที่ครอบคลุมทุกใบไว้ในไฟล์เดียว:

**ผังโปรแกรม**
```
main.dart (Stateless MyApp → MaterialApp)
 └─ LoginPage (StatefulWidget + Form + TextFormField + validator + ElevatedButton)   ← Lab 08, 06
     └─ กด Login ผ่าน → Navigator → HomePage
         └─ DefaultTabController(length: 3)
             ├─ Tab 1: ประวัติ  → SingleChildScrollView + Column
             │           + Image.asset + Text + TextStyle                      ← Lab 04-2, 03-2
             ├─ Tab 2: นับจำนวน → setState + ปุ่ม +/-  + FloatingActionButton  ← Lab 05, 06
             └─ Tab 3: กรอกข้อมูล → TextField/TextFormField + controller      ← Lab 06
-model class  เช่น class Student { String name; int age; ... } extends/override ← Lab 04-1
```

**main.dart ตั้งต้น (ก๊อปไปแก้ต่อได้เลย)**
```dart
import 'package:flutter/material.dart';
import 'login_page.dart';   // เพิ่มเองเมื่อแยกไฟล์

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Exam App',
      theme: ThemeData(useMaterial3: true),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int counter = 0;
  final nameCtrl = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Scaffold(
        appBar: AppBar(
          title: const Text('สอบรวมทุก Lab'),
          bottom: const TabBar(tabs: [
            Tab(icon: Icon(Icons.person), text: 'ประวัติ'),
            Tab(icon: Icon(Icons.add), text: 'นับจำนวน'),
            Tab(icon: Icon(Icons.edit), text: 'กรอกข้อมูล'),
          ]),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () => setState(() => counter = 0),
          child: const Icon(Icons.refresh),
        ),
        body: TabBarView(children: [
          // ---- Tab 1: ScrollView ----
          const SingleChildScrollView(
            child: Column(children: [
              Image.network('https://www.rmutt.ac.th/wp-content/uploads/2023/01/20210202-logo-RMUTT-News-1024x341.png'),
              Padding(
                padding: EdgeInsets.all(16),
                child: Text('ประวัตินักศึกษา\nชื่อ-นามสกุล\nรหัส\nสาขาวิชา\nเกรดเฉลี่ย',
                    textAlign: TextAlign.center,
                    style: TextStyle(fontSize: 18, fontFamily: 'Tahoma')),
              ),
            ]),
          ),
          // ---- Tab 2: setState ----
          Center(
            child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
              Text('$counter', style: const TextStyle(fontSize: 48)),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                ElevatedButton(onPressed: () => setState(() => counter--),
                    child: const Text('-')),
                const SizedBox(width: 16),
                ElevatedButton(onPressed: () => setState(() => counter++),
                    child: const Text('+')),
              ]),
            ]),
          ),
          // ---- Tab 3: Form ----
          Padding(
            padding: const EdgeInsets.all(16),
            child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
              TextField(controller: nameCtrl,
                  decoration: const InputDecoration(labelText: 'ชื่อ',
                      border: OutlineInputBorder())),
              const SizedBox(height: 16),
              Text('พิมพ์ว่า: ${nameCtrl.text}'),   // ใช้ onChanged + setState ให้ขึ้นสด
            ]),
          ),
        ]),
      ),
    );
  }
}
```

**เคล็ดลับตอนทำข้อสอบ**
1. **ไล่ตามใบ Lab** ทีละหัวข้อ อย่าข้าม — ข้อสอบมัก "รวมขั้นตอนจากหลายๆ ใบ" ไว้ในโปรแกรมเดียว
2. ทำ **โครงก่อน** (`main` → MyApp → Scaffold → appBar/body) แล้วค่อยใส่รายละเอียด — ผิดเครื่องหมาย `;` / ปิดวงเล็บ = compile error ทั้งโปรเจค
3. `const` ใส่เฉพาะ widget ที่ไม่มีค่าเปลี่ยน ถ้า VS Code ฟ้องให้ย้าย/ลบ ทำตามทันที
4. ถ้าโจทย์ให้เปลี่ยนหน้าจอ → **StatefulWidget + `setState`** เท่านั้น
5. ถ้ามีรูป → ตรวจ `pubspec.yaml` assets ทุกครั้ง
6. ถ้ามี TextField → อย่าลืม `controller` + `validator` + `_formKey.currentState!.validate()`
7. ชื่อโปรเจค/คลาส: ตัวเล็ก-ขีดล่าง, แก้ชื่อคลาสหลักแล้ว **แก้ `test/widget_test.dart`** ด้วย

---

## 10. 🎤 คำถามปากเปล่า (ถามหลังทำข้อสอบ) — ตอบสั้น ๆ ให้เป็น

**Flutter/Dart พื้นฐาน**
- **Dart ต่างจาก Java/C อย่างไร?** → มี `??`, `?.`, null safety ในตัว, `int/int` ได้ `double`, ทุกคลาสเป็น interface ได้, ใช้ `with` แทน multiple inheritance
- **`final` ต่างจาก `const` ยังไง?** → `final` กำหนดตอน runtime (ห้ามเปลี่ยนภายหลัง), `const` ค่าคงที่ตอน compile-time ต้องเป็น literal
- **`var` ต่างจาก `dynamic`?** → `var` ล็อกชนิดจากค่าครั้งแรกแล้วเปลี่ยนไม่ได้, `dynamic` เปลี่ยนได้ตลอดแต่เสี่ยง runtime error
- **null safety ช่วยอะไร?** → เตือน/บล็อกตอนเรียกค่าที่เป็น null ตั้งแต่ compile ลด null exception ใช้ `?`, `!`, `??`, `?.`
- **String interpolation เขียนยังไง?** → `'$ตัวแปร'` และ `'${expression}'`

**Widget / State**
- **StatelessWidget กับ StatefulWidget ต่างกันยังไง?** → stateless ไม่มีสถานะเปลี่ยนระหว่างรัน, stateful เก็บสถานะได้และอัปเดต UI ผ่าน `setState`
- **ทำไมต้องมี `createState()`?** → Flutter สร้าง object ของ `State` แยกจาก widget เพื่อเก็บสถานะให้ข้ามการ rebuild
- **`setState` ทำหน้าที่อะไร?** → บอก framework ว่าสถานะเปลี่ยน ให้เรียก `build()` ใหม่ — ไม่เรียกก็เปลี่ยนค่าได้แต่ **จอไม่เปลี่ยน**
- **`{super.key}` ใส่ทำไม?** → ส่ง key ขึ้นให้ super class ใช้ระบุตัวตน widget ตอน rebuild/list (จำเป็นใน constructor ของ widget ยุคใหม่)
- **`const` กับ `final` ใน widget?** → `const` ช่วยให้ Flutter ข้ามการสร้าง widget ซ้ำได้ (performance) ใส่เมื่อค่าไม่เปลี่ยน
- **Widget tree คืออะไร?** → โครงสร้างชั้นของ widget ที่ห่อหุ้มกัน เริ่ม `runApp` → MaterialApp → Scaffold → AppBar/Body
- **ทำไมต้องแก้ `widget_test.dart`?** เพราะเทสต์อ้างถึงคลาสหลักเดิม แก้ชื่อคลาสแล้ว test จะ fail

**OOP**
- **4 หลัก OOP?** → Encapsulation, Inheritance, Polymorphism, Abstraction
- **`extends` ต่างจาก `implements`?** → extends สืบทอดทั้ง field+method (มีตัวจริงให้ใช้, เรียก `super` ได้), implements กำหนดเฉพาะรูปแบบ ต้องเขียน method ครบทุกตัว
- **abstract class คือ?** → คลาสที่มี method ไม่มีตัว body `void area();` ใช้เป็นต้นแบบ สร้าง object ตรง ๆ ไม่ได้
- **private ใน Dart?** → ขึ้นต้นด้วย `_` (ไม่มี keyword `private`) เห็นได้เฉพาะในไฟล์เดียวกัน ใช้ getter/setter เข้าถึง
- **mixin / `with` ใช้ตอนไหน?** → ต้องการสืบทอดหลายคลาส (Dart extends ได้คลาสเดียว) — ถ้า `A with B, C` เรียก method ที่ซ้ำจะได้ของ **คลาสขวาสุด**
- **ทำไม `==` ของ object บางทีผิด?** เพราะเก็บแบบ reference → override `operator ==` เทียบค่าจริง

**Layout / ฟอร์ม**
- **Column ต่างจาก Row?** → แนวตั้ง / แนวนอน ใช้ `SizedBox` คั่น, `mainAxisAlignment` จัดแนวตามแกนหลัก
- **`SingleChildScrollView` ใช้ตอนไหน?** เนื้อหายาวกว่าจอ ให้เลื่อนดูได้
- **Tab ทำยังไง?** `DefaultTabController(length:)` → `AppBar(bottom: TabBar(tabs:))` → `body: TabBarView(children:)` ทั้งสามจำนวนต้องเท่ากัน
- **Validator / FormKey ทำงานอย่างไร?** `_formKey.currentState!.validate()` รัน validator ทุก field คืน true ถ้าผ่านหมด
- ** assets รูปภาพ ต้องทำอะไร?** ใส่โฟลเดอร์ +  uncomment `assets:` ใน `pubspec.yaml` + `flutter pub get`
- **AVD เข้า localhost ของเครื่องยังไง?** `10.0.2.2` ( emulator) เช่น `http://10.0.2.2:81/...`
- **HTTP กับ PHP ทำยังไง?** `flutter pub add http` → `await http.post(url, body:{...})` ในฟังก์ชัน `async` ฝั่ง PHP รับ `$_POST` แล้ว echo JSON

---

## 11. Checklist ก่อนวันสอบ (อังคาร)

- [ ] เปิด Android Studio / VS Code + AVD ได้ปกติ (`flutter doctor` ผ่าน)
- [ ] สร้างโปรเจคใหม่ได้เร็ว (Ctrl+Shift+P → Flutter: New Project) และจำได้ว่าชื่อต้องตัวเล็ก
- [ ] เขียนโครง `main → MyApp → Scaffold → appBar/body` จากความจำได้
- [ ] เคยแก้ `test/widget_test.dart` ตามชื่อคลาสใหม่
- [ ] เคยทำ Tab + TabBarView + แยกไฟล์ dart คนละไฟล์ + import
- [ ] เคยทำ SingleChildScrollView + assets + pubspec
- [ ] เคยทำ counter ด้วย `setState` + ปุ่ม TextButton/ElevatedButton
- [ ] เคยทำ Form + TextFormField + validator + controller + Navigator
- [ ] ทวน Dart: control flow, List method, class/getter-setter/extends/implement
- [ ] พกเอกสาร: ใบ Lab ทั้ง 7 ฉบับ + เอกสารสรุปไฟล์นี้ + ตัวอย่างโค้ดที่เคยทำ
- [ ] ซ้อมตอบคำถามปากเปล่าข้อ 10 ออกเสียงดัง ๆ สัก 1 รอบ

**เอกสารที่พกได้ (ตามที่ อ. อนุญาต):** เอกสารเข้าฟ้องสอบได้ → ปริ้นใบ Lab + ไฟล์นี้ติดมือไป ยิ่งมี index/tab แยกหัวข้อยิ่งหาเจเร็ว

---

*สรุปจากไฟล์ใบ Lab ต้นฉบับ: 02 Introduction to Flutter · 03-1 Dart control flow · 03-2 textstyle · 04-1 Class and Inheritance · 04-2 tabmenu/scrollview · 05 Scaffold and StatefulWidget · 06 การใช้วิดเจ็ตพื้นฐาน 1 · 08 flutter login v2*
