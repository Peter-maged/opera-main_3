import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'Header_Screen.dart';
import 'inputWrapper_Screen.dart';

class LoginScreen extends StatelessWidget {
  static const String id = 'login_screen';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: double.infinity,
        decoration: BoxDecoration(
          gradient: LinearGradient(begin: Alignment.topCenter, colors: [
            Colors.cyan[500],
            Colors.cyan[300],
            Colors.cyan[400],
          ]),
        ),
        child: Column(
          children: <Widget>[
            Hero(
              tag: 'logo',
              child: Center(
                child: Container(
                  margin: EdgeInsets.all(60.0),
                  height: 150.0,
                  width: 150.0,
                  child: Column(
                    children: [
                      CircleAvatar(
                        radius: 70.0,
                        backgroundColor: Colors.cyan,
                        backgroundImage: AssetImage('image/appstore1.png'),
                      )
                    ],
                  ),
                ),
              ),
            ),
            Header(),
            Expanded(
              child: Container(
                decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.only(
                      topLeft: Radius.circular(60.0),
                      topRight: Radius.circular(60.0),
                    )),
                child: InputWrapper(),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
