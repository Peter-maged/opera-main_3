import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'inputWrapper1_Screen.dart';
import 'Header1_Screen.dart';

class RegistrationScreen extends StatelessWidget {
  static const String id = 'registration_screen';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: double.infinity,
        decoration: BoxDecoration(
          gradient: LinearGradient(begin: Alignment.topCenter, colors: [
            Colors.blueAccent,
            Colors.blueAccent,
            Colors.blueAccent,
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
