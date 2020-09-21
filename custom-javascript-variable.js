function(){
    try {
        var tracker = ga.getAll()[0];
        return tracker.get('clientId');
      } catch(e) {
        return "n/a";
      }
}