<?php
	$folder = '*';
	$searchFor = 'include';
	$extension = 'php';
	$array = array();
	$i = 0;
	if($folder)
	{
		foreach(glob($folder . sprintf("*.%s", $extension)) as $file)
		{
			if($file != 'output.php')
			{
				$search = 'include';
				$lines = file($file);
				foreach($lines as $line)
				{
					if(strpos($line, $search) !== false)
					{
						if (preg_match('/include \'(.*?)\';/', $line, $match) == 1)
						{
							$imported = $match[1];
    			//			echo '<b>'.$match[1].'</b> jest importowany do <b>'.$file.'</b><br>';
    						$newdata =  array (
								'imported_file' => $imported,
   						    	'source_file' => $file
							);
							$array[$i] = $newdata;

							$i++;
						}	
					}
				}
			}
		}
	}
//	echo '<pre>'; print_r(json_encode($array)); echo '</pre>';
	print_r(json_encode($array));
?>
