public class Chark extends Player {

	public Chark(int posx, int posy, int index, SurvivalGame game) {
		super(100, 4, posx, posy, index, game);

		this.myString = "C" + Integer.toString(index);
		this.Symbol = "C";
		
		if( index == ((game.getN())/2) - 1 ) {
			this.equipment = new Wand(this);
		}
		else{this.equipment = new Axe(this);}

	}

	public void teleport() {
		
		super.teleport();
		if(this.index == ((game.getN())/2) - 1) {
			((Wand)this.equipment).enhance();
		}
		else{
		((Axe) this.equipment).enhance(); }
	}

	@Override
	public void askForMove() {
		// TODO Auto-generated method stub
		
		if(this.equipment instanceof Axe){
		System.out.println(String.format("You are a Chark (C%d) using Axe. (Range: %d, Damage: %d)",this.index,
			this.equipment.getRange(), this.equipment.getEffect()));
		}
		else if(this.equipment instanceof Wand) {
			System.out.println(String.format("You are a Chark (C%d) using Wand. (Range %d, Heal per cast: %d)", this.index, 
				this.equipment.getRange(),
				this.equipment.getEffect() ));

		
		}
		super.askForMove();
	}



}