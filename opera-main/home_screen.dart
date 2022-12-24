import 'package:flutter/material.dart';
class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        margin: EdgeInsets.only(left: 0.0, top: 2.0, right: 0.0, bottom: 0.0),
        padding: EdgeInsets.all(20.0),
        decoration: BoxDecoration(
          image: DecorationImage(
              image: AssetImage("images/download.jpg"),
              fit: BoxFit.fitWidth,
              alignment: Alignment.topLeft),
        ),
      ),
    );
  }
}
