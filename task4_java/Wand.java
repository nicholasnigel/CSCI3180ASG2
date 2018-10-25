public class Wand extends Weapon{
	private static final int WAND_RANGE = 5;
	private static final int WAND_INIT_HEAL = 10;

	public Wand(Player owner)
	{
		super(WAND_RANGE, WAND_INIT_HEAL, owner);
	}


	public void enhance(){

		this.effect += 5;
	}

	@Override
	public void action(int posx, int posy){

		System.out.println("You are using wand to heal " + posx + " " + posy + ".");

		if (this.owner.pos.distance(posx, posy)  <= this.range) {
			// search for all targets with target coordinates.
			Player player = owner.game.getPlayer(posx, posy);

			if(player != null ) 
			{
				if(player.getClass().equals( owner.getClass())){
					player.increaseHealth(this.effect);
					System.out.println("You have healed " + player.myString ); 
				}
				else {
					System.out.println(" The target you're healing is not of the same race");
				}

				
			}
		} else {
			System.out.println("Out of reach.");
		}
	}

}