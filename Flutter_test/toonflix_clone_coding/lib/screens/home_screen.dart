import 'package:flutter/material.dart';
import 'package:toonflix_clone_coding/models/webtoon_model.dart';
import 'package:toonflix_clone_coding/services/api_service.dart';
import 'package:toonflix_clone_coding/widgets/webtoon_widget.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({super.key});

  final Future<List<WebtoonModel>> webtoons = ApiService.getTodaysToons();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          centerTitle: true,
          elevation: 1,
          foregroundColor: Colors.white,
          backgroundColor: Colors.green,
          title: const Text(
            "Today's 툰s",
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.w400),
          ),
        ),
        body: FutureBuilder(
          future: webtoons,
          //The snapshot is future's status.
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              //ListView.builder is optimized version of ListView
              //Load data that users are watching.
              //extract method.
              return Column(
                children: [
                  const SizedBox(
                    height: 50,
                  ),
                  //set constrained height of makeList.
                  Expanded(child: makeList(snapshot))
                ],
              );
            }
            return const Center(
              child: CircularProgressIndicator(),
            );
          },
        ));
  }

  ListView makeList(AsyncSnapshot<List<WebtoonModel>> snapshot) {
    return ListView.separated(
      scrollDirection: Axis.horizontal,
      itemCount: snapshot.data!.length,
      padding: const EdgeInsets.symmetric(
        vertical: 10,
        horizontal: 10,
      ),
      //build an item of ListView.
      itemBuilder: (context, index) {
        print(index);
        var webtoon = snapshot.data![index];
        return Webtoon(
          title: webtoon.title,
          thumb: webtoon.thumb,
          id: webtoon.id,
        );
      },
      //separte data. in this case, A SizedBox is used.
      separatorBuilder: (context, index) => const SizedBox(
        width: 40,
      ),
    );
  }
}
